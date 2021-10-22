const headers = ['Image', 'Filename', 'Size', 'Result'];

function hiddenforms(data) {
    const form = document.createElement('form');
    form.method = 'POST';
    form.action = '/infer';
    form.enctype = 'multipart/form-data';
    form.style.visibility='hidden';
    const hiddenField = document.createElement('input');
    hiddenField.type = 'file';
    hiddenField.name = 'file';
    hiddenField.accept =".jpg, .jpeg, .png"
    hiddenField.class="custom-file-input" 
    hiddenField.id="inputGroupFile"
    hiddenField.files = data
    form.appendChild(hiddenField);
    document.body.appendChild(form);
    form.submit();
    document.body.removeChild(form);
}

if (window.FileReader) {
    var drop;
    addEventHandler(window, 'load', function () {
        drop = document.getElementById('drop');
        var count = 0

        function cancel(e) {
            if (e.preventDefault) {
                e.preventDefault();
            }
            return false;
        }

        // Tells the browser that we *can* drop on this target
        addEventHandler(drop, 'dragover', cancel);
        addEventHandler(drop, 'dragenter', cancel);

        addEventHandler(drop, 'drop', function (e) {
            e = e || window.event; // get window.event if e argument missing (in IE)   
            if (e.preventDefault) {
                e.preventDefault();
            } // stops the browser from redirecting off to the image.

            var dt = e.dataTransfer;
            var files = dt.files;

            if (files.length > 3 || count > 3) {
                alert('Maximum 3 image allowed')
            }
            else {
                hiddenforms(files)
            }
            return false;
        });

        Function.prototype.bindToEventHandler = function bindToEventHandler() {
            var handler = this;
            var boundParameters = Array.prototype.slice.call(arguments);
            //create closure
            return function (e) {
                e = e || window.event; // get window.event if e argument missing (in IE)   
                boundParameters.unshift(e);
                handler.apply(this, boundParameters);
            }
        };
    });
}

function addEventHandler(obj, evt, handler) {
    if (obj.addEventListener) {
        // W3C method
        obj.addEventListener(evt, handler, false);
    } else if (obj.attachEvent) {
        // IE method.
        obj.attachEvent('on' + evt, handler);
    } else {
        // Old school method.
        obj['on' + evt] = handler;
    }
}
