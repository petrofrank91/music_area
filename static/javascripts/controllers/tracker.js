'user strict';

angular.module('tracker')
    .controller('trackerCtrl',['$scope', '$rootScope', '$timeout', '$interval', '$location', 'TrackerService',
function ($scope, $rootScope, $timeout, $interval, $location, TrackerService) {

    function getParameterByName(name) {
        name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
        var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
            results = regex.exec(location.search);
        return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
    }

    $scope.MUSIC_COUNT = 3;

    $scope.isMusicPlay = true;
    $scope.playStep = 1;
    $scope.playProgress = 0;
    $scope.testCompleted = false;
    $scope.isSkip = false;
    $scope.feedbackData = {};
    $scope.session_id = getParameterByName('session_id');
    $scope.testMusics = [];

    var stop;

    function stopPlayer () {
        $interval.cancel(stop);
    }

    function startPlayer () {
        stop = $interval( function() {
            if ($scope.playProgress == 100) {
                $scope.next();
            } else {
                $scope.playProgress += 2;
            }
        }, 100);
    }

    function resetFeedbackData () {
        $scope.feedbackData.isHeard = 'true';
        $scope.feedbackData.skipReason = 'NOT_INTERESTING';
    }

    $scope.skip = function () {
        stopPlayer();
        $scope.isMusicPlay = false;
        $scope.playProgress = 0;
        $scope.isSkip = true;
    };

    $scope.next = function () {
        stopPlayer();
        $scope.isMusicPlay = false;
        $scope.playProgress = 0;
        $scope.isSkip = false;
    };

    $scope.feedback = function () {
        TrackerService.createPlay({
            'musaic': $scope.testMusics[$scope.playStep-1].id,
            'session': $scope.session_id,
            'is_skipped': $scope.isSkip,
            'is_listened_before': $scope.feedbackData.isHeard === "true" ? true : false,
            'listened_ratio': 1,
            'skipping_reason': $scope.feedbackData.skipReason
        }).then(function () {
            if ( $scope.playStep !== $scope.MUSIC_COUNT ) {
                $scope.playStep++;
                $scope.isMusicPlay = true;
                startPlayer();
            } else {
                $scope.testCompleted = true;
            }
            resetFeedbackData();
        }, function() {
            alert('Can not l;');
        });
    };

    $scope.init = function() {
        TrackerService.getMusics().then(function(result) {
            if (result && result.data && result.data.results && result.data.results.length > 0) {
                $scope.testMusics = angular.copy(result.data.results);
                $scope.MUSIC_COUNT = result.data.results.length;
                startPlayer();
            } else {
                alert('Can not load musics');
                $scope.testCompleted = true;
            }
        }, function() {
            alert('Can not load musics');
            $scope.testCompleted = true;
        });
        resetFeedbackData();
    };

    $scope.init();
}]);