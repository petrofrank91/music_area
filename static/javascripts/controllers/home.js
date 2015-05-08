'user strict';

angular.module('tracker').controller('homeCtrl',['$scope', '$rootScope', '$location', 'TrackerService',
    function ($scope, $rootScope, $location, TrackerService) {
    $scope.startTest = function () {
        TrackerService.createSession({
            referral_link: 'http://referal.link.com' + (new Date()).getTime(),
            referral_code: (new Date()).getTime()
        }).then(function(response) {
            if (response && response.data) {
                location.href= '/tracker/?session_id=' + response.data.id;
            } else {
                alert('Could not create a new session.');
            }
        });
    };
}]);