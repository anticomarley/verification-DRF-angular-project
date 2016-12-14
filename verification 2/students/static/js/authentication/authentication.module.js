(function () {
  'use strict';

  angular
    .module('everify.authentication', [
      'everify.authentication.controllers',
      'everify.authentication.services'
    ]);

  angular
    .module('everify.authentication.controllers', []);

  angular
    .module('everify.authentication.services', ['ngCookies']);
})();