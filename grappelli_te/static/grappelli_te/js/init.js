
// Why must this be declared globally, KO?
var VM;
(function($) {
    $(document).ready(function () {
        var editor = CodeMirror.fromTextArea(document.getElementById('editor'), {
            mode: "text/html",
            lineWrapping: true,
            lineNumbers: true
        });

        VM = {
            rootNode: ko.observableArray([]),
            refreshList: function () {
                $.getJSON('list/', function (data) {
                    VM.rootNode(data);
                });
            },
            openFile: function () {
                if(this.open !== undefined) { return false; }
                if(!editor.isClean() ) {
                    if(!window.confirm('Current document is not saved.  Are you sure?')) { return False; }
                }
                var self = this;
                $.get('open/', {path: this.path}, function (data) {
                    editor.setValue(data);
                    editor.markClean();
                    $('[name=name]').val(self.path);
                });
                return true;
            },
            saveFile: function () {
                $.post('open/', {
                    path: $('[name=name]').val(),
                    data: editor.getValue()
                }, function () {
                    editor.markClean();
                    VM.refreshList(); // in case we created a new one
                });
            },
            closeFile: function () {
                if(!editor.isClean()) {
                    if(!window.confirm('Current document is not saved.  Are you sure?')) { return False; }
                }
                editor.setValue('');
                editor.markClean();
                $('[name=name]').val('');
            }
        };

        ko.applyBindings(VM);
        VM.refreshList();

    });
})(grp.jQuery);

