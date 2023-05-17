// custom js file for the ecommerce app
// custom model toast
function showModal(title, body, btnText, btnClass, btnLink) {
    $('#modal-title').html(title);
    $('#modal-body').html(body);
    $('#modal-btn').html(btnText);
    $('#modal-btn').addClass(btnClass);
    $('#modal-btn').attr('href', btnLink);
    $('#modal').modal('show');
}
function showToast(title, body, icon, delay) {
    $('#toast-title').html(title);
    $('#toast-body').html(body);
    $('#toast-icon').addClass(icon);
    $('#toast').toast({delay: delay});
    $('#toast').toast('show');
}
function formatPrice(price) {
    return price.toLocaleString('en-US', {style: 'currency', currency: 'USD'});
}
function formatRating(rating) {
    return rating.toFixed(1);
}
function formatDateTime(date) {
    return date.toLocaleString();
}
function formatDateTimeShort(date) {
    return date.toLocaleString('en-US', {month: 'short', day: 'numeric', year: 'numeric'});
}
function formatDateTimeLong(date) {
    return date.toLocaleString('en-US', {month: 'long', day: 'numeric', year: 'numeric'});
}
function customModelDelete(title, body, btnText, btnClass, btnLink) {
    $('#modal-title').html(title);
    $('#modal-body').html(body);
    $('#modal-btn').html(btnText);
    $('#modal-btn').addClass(btnClass);
    $('#modal-btn').attr('onclick', btnLink);
    $('#modal').modal('show');
}

// custom model toast
toast = (title, body, icon, delay) => {
    $('#toast-title').html(title);
    $('#toast-body').html(body);
    $('#toast-icon').addClass(icon);
    $('#toast').toast({delay: delay});
    $('#toast').toast('show');
}
