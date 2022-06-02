function hideLoader(el) {
    if (IsImageOk(el) == true) {
        console.log(IsImageOk(el));
        hideLoading(el);
    }
}

function IsImageOk(img) {
    if (!img.complete) {
        return false;
    }
    else if (typeof img.naturalWidth != "undefined" && img.naturalWidth == 0) {
        return false;
    } 
    else {
        return true;
    }
}

function hideLoading(el) {
    el.previousElementSibling.remove();
}