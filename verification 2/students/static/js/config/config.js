(function () {
  'use strict';

  angular
    .module('everify.config')
    .config(config);
    .run(run);

  config.$inject = ['$locationProvider', '$httpProvider', '$interpolateProvider'];
  run.$inject = ['$http', '$cookies'];


  /**
  * @name config
  * @desc Enable HTML5 routing
  */
  function config($locationProvider, $httpProvider, $interpolateProvider) {
    $locationProvider.html5Mode(true);
    $locationProvider.hashPrefix('!');
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
  }

  /**
* @name run
* @desc Update xsrf $http headers to align with Django's defaults
*/
  function run($http, $cookies) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
    //$http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
  }
})();