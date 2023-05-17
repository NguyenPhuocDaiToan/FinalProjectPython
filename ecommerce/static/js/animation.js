// custom animation for the ecommerce site
function scrollToActivePage() {
    // get the active page
    var activePage = document.getElementsByClassName("active")[0];
    // scroll to the active page
    activePage.scrollIntoView({behavior: "smooth", block: "start", inline: "nearest"});
}

function scrollToTop() {
    // scroll to the top of the page
    window.scrollTo({top: 0, behavior: "smooth"});
}

function scrollToBottom() {
    // scroll to the bottom of the page
    window.scrollTo({top: document.body.scrollHeight, behavior: "smooth"});
}

function lazyLoading() {
    // get all the images
    var images = document.getElementsByTagName("img");
    // loop through all the images
    for (var i = 0; i < images.length; i++) {
        // check if the image is not loaded
        if (!images[i].hasAttribute("src")) {
            // set the image source
            images[i].setAttribute("src", images[i].getAttribute("data-src"));
        }
    }
}

function showLoading() {
    // show the loading animation
    document.getElementById("loading").style.display = "block";
}

function hideLoading() {
    // hide the loading animation
    document.getElementById("loading").style.display = "none";
}

function showLoadingBtn() {
    // show the loading button
    document.getElementById("loading-btn").style.display = "block";
}

function hideLoadingBtn() {
    // hide the loading button
    document.getElementById("loading-btn").style.display = "none";
}

function handleError(error) {
    // show the error message
    document.getElementById("error").innerHTML = error;
    document.getElementById("error").style.display = "block";
}

