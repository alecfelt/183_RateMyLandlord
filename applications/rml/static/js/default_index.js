// This is the js for the default/index.html view.

$(window).on("load", function() {
  $('.main-content').css('opacity', '1');
});

// components

var HomePage = {
  template: `
  `
}, WriteReview = {
  template: `
    <div class="search">
      <form class="search-form">
        <input id="search-box" type="search" placeholder="Search for a Landlord or Property"/>
        <button id="search-button">
          <i class="fa fa-search"></i>
        </button>
      </form>
    </div>
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
  // 'landlord_page': LandlordPage, on the html it has landlord-page
  'landlord-page': LandlordPage,
  'landlord-review': LandlordReview,
  'house-review': HouseReview
}

var app = function() {

  var self = {};

  Vue.config.silent = false; // show all warnings

  self.change_page = function(page) {
    console.log(page);
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
