// This is the js for the default/index.html view.

$(window).on("load", function() {
  $('.main-content').css('opacity', '1');
});

// components

Vue.component('HomePage', {
  template: `
    <div> HomePage </div>
  `
});
Vue.component('WriteReview', {
  props: ['landlord'],
  template: `
    <div class="sub-page">
      <div class="write-review-card">
        <h1> Write a Review </h1>
        <form action="#" v-on:submit.prevent="add_review" class="review-items">
          <div>
            <input
              placeholder="Memo Title: left these the same for now"
              v-model="form_title"
              name="title"
              type="text" />
          </div>

          <div>
            <input
              placeholder="Memo Content"
              v-model="form_body"
              name="body"
              type="text" />
          </div>

          <div>
              <p> Rate your landlord </p>
              <select v-model="form_landlord_rating">
                  <option selected="true" disabled="true">
                      please select
                  </option>
                  <option value="1"> 1 </option>
                  <option value="2"> 2 </option>
                  <option value="3"> 3 </option>
                  <option value="4"> 4 </option>
                  <option value="5"> 5 </option>
              </select>
          </div>

          <div>
              <p> Rate your property </p>
              <select v-model="form_property_rating">
                  <option selected="true" disabled="true">
                      please select
                  </option>
                  <option value="1"> 1 </option>
                  <option value="2"> 2 </option>
                  <option value="3"> 3 </option>
                  <option value="4"> 4 </option>
                  <option value="5"> 5 </option>
              </select>
          </div>

          <div>
              <p> is this a landlord or a land management group </p>
              <select v-model="form_is_landlord">
                  <option value="landlord"> landlord </option>
                  <option value="group/org/ect"> group/org/ect </option>
              </select>
          </div>

          <div>
              <p> How would you rate your landlord's responsiveness? </p>
              <div>
                 <select v-model="form_responsiveness">
                      <option selected="true" disabled="true">
                          perhaps we can fill this with fun descriptive words
                          similar to RMP
                      </option>
                      <option value="1"> 1 </option>
                      <option value="2"> 2 </option>
                      <option value="3"> 3 </option>
                      <option value="4"> 4 </option>
                      <option value="5"> 5 </option>
                  </select>
              </div>
          </div>

          <div>
              <p> Would you rent with this landlord again?<p>
              <div>
                  <input type="radio" name="land" value="yes" v-model="form_rent_landlord_again">yes!<br>
                  <input type="radio" name="land" value="no" v-model="form_rent_landlord_again">no!<br>
              </div>
          </div>

          <div>
              <p> Would you rent this propery again? </p>
              <div>
                  <input type="radio" name="rent" value="yes">yes!<br>
                  <input type="radio" name="rent" value="no">no!<br>
              </div>
          </div>

          <div>
              <p> chill? </p>
              <div>
                  <input type="radio" name="chill"> yas <br>
                  <input type="radio" name="chill"> yesn't <br>
              </div>
          </div>

          <div>
              <p>
                  please select from a list of tags that you think you'd find helpful
                  perhaps this could also take in user #hashtags or something cool.
              </p>
              <div>
                  <ul>
                      <li>pets allowed</li>
                      <li>show up unannounced</li>
                      <li>lives far away</li>
                      <li>accepts venmo</li>
                      <li>. . . if this list goes longer the footer covers sumbit button</li>
                      <li>write your own?</li>
                  </ul>
              </div>
          </div>

          <div>
              <p> Your unique experience </p>
              <textarea v-model="form_review_body">

              </textarea>
          </div>

          <div class="new_memo_buttons">
            <div class="form-group" id="submit_memo">
              <div>
                <input class="btn btn-primary " id="add_memo_btn" type="submit" value="Post This Memo" />
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
  `
});
Vue.component('FindLandlord', {
  props: ['on_select', 'nav_to_create_landlord'],
  data: function() {
    return {
      has_searched: false,
      search_results: []
    }
  },
  methods: {
    handle_search: function(event) {
      var search_str = event.target.search_box.value;
      console.log(search_str);
      $.post(search_landlords_url,
        {
          search_str: search_str
        },
        function(data) {
          console.log(data);
        }
      );
      // async query
        // in callback function
          // has_search = true; search_results = data.search_results;
    }
  },
  template: `
    <div>
      <div class="search">
        <form @submit.prevent="handle_search" class="search-form">
          <input id="search_box" type="search" placeholder="Search for a Landlord"/>
          <button type="submit" id="search-button">
            <i class="fa fa-search"></i>
          </button>
        </form>
      <div>

      <div>
        <p>
          didnt find what you are looking for?
          <a href="#" @click.prevent="nav_to_create_landlord">
            Add A Landlord
          </a>
        </p>
      </div>
    </div>
  `
});
Vue.component('FindProperty', {
  template: `
    <div> FindHouse </div>
  `
});
Vue.component('LandlordPage', {
  props: ['landlord', 'nav_to_write_review'],
  template: `
    <div class="sub-page">
      <a href="#" @click.prevent="nav_to_write_review(landlord)">
        write review for this landlord
      </a>
      <div class="rating-card">
        <h1>Landlord Name McNamey</h1>
        <div class="rating-items">
          <div class="ratings">
            <h2>Overall Rating</h2>
            <p>5.0</p>
          </div>
          <div class="ratings-extras">
            <h3>Average Property Rating</h3>
            <p>5.0</p>
            <h3>Responsiveness</h3>
            <p>5.0</p>
            <h3>Certified Slumlord?</h3>
            <p>No</p>
          </div>
          <div class="ratings-tags">
            <h3>Tags for this Landlord</h3>
            <ul>
              <li>Tag Items would go here</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  `
});
Vue.component('CreateLandlord', {
    template: `
      <div>
          <h1> Add New Landlord </h1>
          <form action="#" class="review-items">

            <div>
              <input
                placeholder="Name of Landlord/Management Group"
                type="text" />
            </div>

            <div>
              <input
                placeholder="Landlord website (optional)"
                type="text" />
            </div>

            <button type="submit">
              <i class="fa fa-plus"></i>
            </button>
          </form>
      </div>
    `
});


var app = function() {

  var self = {};

  Vue.config.silent = false; // show all warnings

  self.nav_to_find_landlord_to_review = function() {
    self.vue.page = self.vue.FIND_LANDLORD_TO_REVIEW;
  }

  self.nav_to_find_landlord_page = function(landlord) {
    self.vue.selected_landlord = landlord;
    self.vue.page = self.vue.FIND_LANDLORD_PAGE;
  }

  self.nav_to_find_property = function() {
    self.vue.page = self.vue.FIND_PROPERTY;
  }

  self.nav_to_create_landlord = function() {
    self.vue.page = self.vue.CREATE_LANDLORD;
  }

  self.nav_to_home_page = function() {
    self.vue.page = self.vue.HOME_PAGE;
  }

  self.nav_to_landlord_page = function() {
    self.vue.page = self.vue.LANDLORD_PAGE;
  }

  self.nav_to_write_review = function(landlord) {
    self.vue.selected_landlord = landlord;
    self.vue.page = self.vue.WRITE_REVIEW;
  }

  // Complete as needed.
  self.vue = new Vue({
    el: "#vue-div",
    delimiters: ['${', '}'],
    unsafeDelimiters: ['!{', '}'],
    data: {
      page: 0,
      HOME_PAGE: 0,
      FIND_LANDLORD_TO_REVIEW: 1,
      FIND_LANDLORD_PAGE: 2,
      FIND_PROPERTY: 3,
      LANDLORD_PAGE: 4,
      CREATE_LANDLORD: 5,
      WRITE_REVIEW: 6,
      selected_landlord: null
    },
    methods: {
      nav_to_find_landlord_to_review: self.nav_to_find_landlord_to_review,
      nav_to_find_landlord_page: self.nav_to_find_landlord_page,
      nav_to_find_property: self.nav_to_find_property,
      nav_to_create_landlord: self.nav_to_create_landlord,
      nav_to_home_page: self.nav_to_home_page,
      nav_to_landlord_page: self.nav_to_landlord_page,
      nav_to_write_review: self.nav_to_write_review
    }
  });

  $("#vue-div").show();
  return self;

};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});
