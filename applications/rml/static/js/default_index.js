// This is the js for the default/index.html view.

// components

var HomePage = {
  template: `
    <div> HomePage </div>
  `
}, WriteReview = {
  template: `
    <div> WriteReview </div>
  `
}, FindLandlord = {
  template: `
    <div> FindLandlord </div>
  `
}, FindHouse = {
  template: `
    <div> FindHouse </div>
  `
}, HousePage = {
  template: `
    <div> HousePage </div>
  `
}, LandlordPage = {
  template: `
    <div> LandlordPage </div>
  `
}, LandlordReview = {
  template: `
    <div> LandlordReview </div>
  `
}, HouseReview = {
  template: `
    <div> HouseReview </div>
  `
}

var components = {
  'home-page': HomePage,
  'write-review': WriteReview,
  'find-landlord': FindLandlord,
  'find-house': FindHouse,
  'house-page': HousePage,
  'landlord_page': LandlordPage,
  'landlord-review': LandlordReview,
  'house-review': HouseReview
}

var app = function() {

  var self = {};

  Vue.config.silent = false; // show all warnings

  self.change_page = function(page) {
    self.vue.page = page;
  }

  // Complete as needed.
  self.vue = new Vue({
    el: "#vue-div",
    delimiters: ['${', '}'],
    unsafeDelimiters: ['!{', '}'],
    data: {
      page: 0,
      logged_in: false
    },
    methods: {
      change_page: self.change_page
    },
    components: components
  });

  return self;

};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});
