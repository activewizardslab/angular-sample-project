$(document).ready(function() {    
    $('#change-name-form').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            first_name: {
                message: 'The first name is not valid',
                validators: {
                    notEmpty: {
                        message: 'The first name is required and can\'t be empty'
                    },
                    regexp: {
                        regexp: /^[a-zA-Z]+$/,
                        message: 'The first name can only consist of alphabetical'
                    },
                    stringLength: {
                        min: 1,
                        max: 64,
                        message: 'The username must be more than 1 and less than 64 characters long'
                    },
                }
            },
            last_name: {
                message: 'The last name is not valid',
                validators: {
                    notEmpty: {
                        message: 'The last name is required and can\'t be empty'
                    },
                    regexp: {
                        regexp: /^[a-zA-Z]+$/,
                        message: 'The last name can only consist of alphabetical'
                    },
                    stringLength: {
                        min: 1,
                        max: 64,
                        message: 'The username must be more than 1 and less than 64 characters long'
                    },
                }
            }
        }
    });

    $('#change-pwd-form').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            new_password: {
                validators: {
                    notEmpty: {
                        message: 'The password is required and can\'t be empty'
                    },
                    stringLength: {
                        min: 8,
                        max: 30,
                        message: 'The password must be more than 8 and less than 30 characters long'
                    },
                    identical: {
                        field: 'confirm_new_password',
                        message: 'The password and its confirm are not the same'
                    }
                }
            },
            confirm_new_password: {
                validators: {
                    notEmpty: {
                        message: 'The confirm password is required and can\'t be empty'
                    },
                    identical: {
                        field: 'new_password',
                        message: 'The password and its confirm are not the same'
                    }
                }
            }
        }
    });
});
