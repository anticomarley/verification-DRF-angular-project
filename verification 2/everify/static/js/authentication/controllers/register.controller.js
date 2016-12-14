/**
* Register controller
* @namespace everify.controllers
*/
(function () {
  'use strict';

  angular
    .module('everify.authentication.controllers')
    .controller('RegisterController', RegisterController);

  RegisterController.$inject = ['$location', '$scope', 'Authentication'];

  /**
  * @namespace RegisterController
  */
  function RegisterController($location, $scope, Authentication) {
    var vm = this;

    vm.register = register;
    vm.message = 'This is the about page body';
    
    activate();

    /**
     * @name activate
     * @desc Actions to be performed when this controller is instantiated
     * @memberOf authentication.controllers.RegisterController
     */
    function activate() {
      // If the user is authenticated, they should not be here.
      if (Authentication.isAuthenticated()) {
        $location.url('/');
      }
    }

    /**
    * @name register
    * @desc Register a new user
    * @memberOf authentication.controllers.RegisterController
    */
    function register(isValid) {
      /**
      vm.studentform.isSubmitted = true;
      // check to make sure the form is completely valid
      if (isValid) {
        alert('our form is amazing');
        Authentication.register(vm.email, vm.password, vm.username);
      }
      **/
      Authentication.register(vm.email, vm.password, vm.username);
    }


  }
})();
