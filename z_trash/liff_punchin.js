window.onload = function() {
    const defaultLiffId = "";   // change the default LIFF value if you are not using a node server

    // DO NOT CHANGE THIS
    let myLiffId = "";

    myLiffId = defaultLiffId;
    initializeLiffOrDie(myLiffId);
};

/**
* Check if myLiffId is null. If null do not initiate liff.
* @param {string} myLiffId The LIFF ID of the selected element
*/
function initializeLiffOrDie(myLiffId) {
    if (!myLiffId) {
        document.getElementById("liffAppContent").classList.add('hidden');
        document.getElementById("liffIdErrorMessage").classList.remove('hidden');
    } else {
        initializeLiff(myLiffId);
    }
}

/**
* Initialize LIFF
* @param {string} myLiffId The LIFF ID of the selected element
*/
function initializeLiff(myLiffId) {
    liff
        .init({
            liffId: myLiffId
        })
        .then(() => {
            // start to use LIFF's api
            initializeApp();
        })
}

/**
 * Initialize the app by calling functions handling individual app components
 */
function initializeApp() {
    // displayIsInClientInfo();
    registerButtonHandlers();

    // check if the user is logged in/out, and disable inappropriate button
}


/**
* Register event handlers for the buttons displayed in the app
*/
function registerButtonHandlers() {
    var requestURL = "getUserName";
    var token = '{{csrf_token}}';
    if (liff.isLoggedIn()) {
        document.getElementById('liffLoginButton').disabled = true;
        $('#Puncharea')[0].style.display = 'block';
        
        liff.getProfile().then(function(profile) {

            $.ajax({
                headers: { "X-CSRFToken": token },
                url: requestURL,
                data: {"data":profile.userId},
                type: "GET",
                dataType: "html",
                success: function(returnData){
                    document.getElementById('username').textContent = returnData
                    // console.log(returnData);
                    // x.innerHTML = returnData
                },
                error: function(xhr, ajaxOptions, thrownError){
                    document.getElementById('username').textContent = '無名氏'
                    console.log(xhr.status);
                    console.log(thrownError);
                }});

        }).catch(function(error) {
            window.alert('Error getting profile: ' + error);
        })
        // console.log(userID)
        
    
    } else {
        document.getElementById('liffLogoutButton').disabled = true;
        $('#Puncharea')[0].style.display = 'none';
    }
    // get access token
    function aaa() {
        if (!liff.isLoggedIn() && !liff.isInClient()) {
            alert('To get an access token, you need to be logged in. Please tap the "login" button below and try again.');
        } else {
            const accessToken = liff.getAccessToken();
            // document.getElementById('accessTokenField').textContent = accessToken;
            toggleAccessToken();
        }
    };
    document.getElementById('liffLoginButton').addEventListener('click', function() {
        if (!liff.isLoggedIn()) {
            // set `redirectUri` to redirect the user to a URL other than the front page of your LIFF app.
            liff.login();
        }
    });
    // logout call only when external browse
    document.getElementById('liffLogoutButton').addEventListener('click', function() {
        if (liff.isLoggedIn()) {
            liff.logout();
            window.location.reload();
        }
    });
}
