angular.module('tracker').factory('TrackerService', function($http, $q) {
  return {
      /**
       * Create a New TestSession
       * @param param :
       *           object {
       *                referral_link
       *                referral_code
       *           }
       * @returns {HttpPromise}
       */
      createSession: function (param) {
          return $http.post('/api/testsession/', param);
      },

      /**
       * Create a New TestPlay
       * @param param :
       *           {
       *                "musaic": null,
       *                "session": null,
       *                "is_skipped": false,
       *                "is_listened_before": false,
       *                "listened_ratio": null,
       *                "skipping_reason": null
       *            }
       * @returns {HttpPromise}
       */
      createPlay: function (param) {
          return $http.post('/api/testplay/', param);
      },

      /**
       * Get Music List
       * @returns {HttpPromise}
       * @example :
       *        [
       *            {
       *                "id": 5,
       *                "name": "abc"
       *            },
       *            {
       *                "id": 6,
       *                "name": "eee"
       *            },
       *            {
       *                "id": 7,
       *                "name": "fffffff"
       *            },
       *            {
       *                "id": 8,
       *                "name": "ccccccccc"
       *            }
       *        ]
       */
      getMusics: function () {
          return $http.get('/api/musicfile/?page_size=3');
      }
  };
});