(function () {
  'use strict';

  angular
    .module('everify', [
      'everify.config',
      'everify.routes',
      'everify.authentication',
      'everify.layout'
    ]);

  angular
    .module('everify.config', []);
    .module('everify.routes', ['ngRoute']);
})();

