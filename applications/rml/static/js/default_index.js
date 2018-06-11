// This is the js for the default/index.html view.

$(window).on("load", function() {
  $('.main-content').css('opacity', '1');
});

// components

Vue.component('HomePage', {
  props: ['on_select',
          'nav_to_find_landlord_to_review',
          'nav_to_find_landlord_page',
          'nav_to_find_property',
          'landlord_list',
          'toggle_selected_landlord',],
  methods: {
    handle_landlord_select: function(result) {
      this.toggle_selected_landlord(result);
      this.on_select();
    }
  },
  template:
  `
    <div class="sub-page">
      <div class="call-to-action">
        <h1>What are you looking for?</h1>
        <div class="landing-buttons">
          <button @click.prevent="nav_to_find_landlord_page">Find a<br/><b>Landlord</b></button>
          <button @click.prevent="nav_to_find_property">Find a<br/><b>Property</b></button>
          <button @click.prevent="nav_to_find_landlord_to_review">Write a<br/><b>Review</b></button>
        </div>
      </div>
      <h1 v-if="(landlord_list.length!=0)" style="margin:0; margin-bottom: -16pt;">Recently Added Landlords</h1>
      <div class="search-results">
        <div @click.prevent="handle_landlord_select(landlord.first_name)" v-for="landlord in landlord_list.slice(0, 5)" class="search-result">
          <h1>{{landlord.first_name}} {{landlord.last_name}}</h1>
          <div class="rating-items">
            <div class="ratings">
              <h3>Overall Rating</h3>
              <p>5.0</p>
            </div>
            <div class="ratings">
              <h3>Average Property Rating</h3>
              <p>5.0</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  `
});
Vue.component('WriteReview', {
  props: ['landlord', 'nav_to_landlord_page', 'PROPERTY_TAGS', 'LANDLORD_TAGS'],
  methods: {
    add_review: function() {
      if(this.validate_review()) {
        this._data.landlord_id = this.landlord.id;
        var that = this;
        $.post(add_review_url,
          this._data,
          function(data) {
            if(data == "ok"){
              that.nav_to_landlord_page(that.landlord.id);
            }
          }
        );
      }
    },
    validate_review() {
      for(var key in this._data) {
        if(this._data[key] == null) {
          return false;
        }
      }
      var regex = /^[A-Za-z][A-Za-z]$/;
      if(regex.exec(this._data.state) == null) {
        return false;
      }
      return true;
    },
    handle_landlord_tag(event) {
      console.log(event);
    },
    handle_property_tag(event) {
      console.log(event);
    }
  },
  data: function() {
    return {
      street: null,
      city: null,
      state: null,
      zip: null,
      landlord_rating: 1,
      property_rating: 1,
      rent_with_landlord_again: null,
      rent_with_property_again: null,
      landlord_tag_ids: [],
      property_tag_ids: [],
      comments: null
    }
  },
  template: `
    <div class="sub-page">
      <div class="write-review-card">
        <h1> Write a Review for {{landlord.first_name}}</h1>
        <form action="#" v-on:submit.prevent="add_review" class="review-items">
          <div>
            <p> Property </p>
            <p> Street </p>
              <input
                placeholder="street"
                v-model="street"
                name="address"
                type="text" />
            <p> City </p>
              <input
                placeholder="city"
                v-model="city"
                name="address"
                type="text" />
            <p> State </p>
              <input
                placeholder="state"
                v-model="state"
                name="address"
                type="text" />
            <p> Zip </p>
              <input
                placeholder="zip"
                v-model="zip"
                name="address"
                type="text" />
          </div>
          <div>
              <p> Rate your landlord </p>
              <select v-model="landlord_rating">
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
              <select v-model="property_rating">
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
              <p> Would you rent with this landlord again?<p>
              <div>
                  <input type="radio" name="land" value="yes" v-model="rent_with_landlord_again">yes!<br>
                  <input type="radio" name="land" value="no" v-model="rent_with_landlord_again">no!<br>
              </div>
          </div>

          <div>
              <p> Would you rent this propery again? </p>
              <div>
                  <input type="radio" name="rent" value="yes" v-model="rent_with_property_again">yes!<br>
                  <input type="radio" name="rent" value="no" v-model="rent_with_property_again">no!<br>
              </div>
          </div>

          <div>
              <p>
                  please select from a list of tags that you think you'd find helpful.
              </p>
              <div id="landlord-tags-container">
                  <p> Landlord Tags </p>
                  <ul>
                      <li
                          v-for="tag in LANDLORD_TAGS"
                          v-on:click="handle_landlord_tag">
                              {{tag}}
                      </li>
                  </ul>
              </div>
              <div id="landlord-tags-container">
                  <p> Property Tags </p>
                  <ul>
                      <li
                          v-for="tag in PROPERTY_TAGS"
                          v-on:click="handle_property_tag">
                              {{tag}}
                      </li>
                  </ul>
              </div>
          </div>

          <div>
              <p> Your unique experience </p>
              <textarea v-model="comments">

              </textarea>
          </div>

          <div class="new_review_buttons">
            <div class="form-group" id="submit_review">
              <div>
                <input class="btn btn-primary " id="add_review_btn" type="submit" value="Post This Review" />
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
  `
});
Vue.component('FindLandlord', {
  props: ['on_select',
          'nav_to_create_landlord',
          'set_search_results',
          'search_results',
          'toggle_selected_landlord',
          'nav_to_write_review',
        ],
  methods: {
    handle_search: function(event) {
      var search_str = event.target.value;
      console.log("Searching for " + search_str);
      var that = this;
      $.post(search_landlords_url,
        {
          search_str: search_str
        },
        function(data) {
          console.log("Recieved: ");
          console.log(data.landlords); // Data is here
          that.set_search_results(data.landlords);
          $('#search-button').prop('enabled', true);
        }
      );
    },
    handle_landlord_select: function(result) {
      this.toggle_selected_landlord(result);
      this.on_select();
    }
  },
  template:
  `
    <div class="sub-page">
      <div class="search">
        <h4 v-if="on_select === nav_to_write_review">Step 1: Find the landlord you wish to review</h4>
        <form class="search-form">
          Search for a landlord:
          <input v-on:input="handle_search" id="search_box" type="search" placeholder="Search happens in real-time so type away!"/>
        </form>
        <div v-if="search_results.length != 0" class="search-results">
          <div @click.prevent="handle_landlord_select(result)" v-for="result in search_results" class="search-result">
            <h1>{{result.first_name}} {{result.last_name}}</h1>
            <div class="rating-items">
              <div class="ratings">
                <h3>Overall Rating</h3>
                <p>5.0</p>
              </div>
              <div class="ratings">
                <h3>Average Property Rating</h3>
                <p>5.0</p>
              </div>
            </div>
          </div>
        </div>
        <div class="search-prompt">
          <p>
            didn't find what you are looking for?
            <a href="#" @click.prevent="nav_to_create_landlord">
              Add A Landlord
            </a>
          </p>
        </div>
      <div>
    </div>
  `
});
Vue.component('FindProperty', {
  props: [
          'nav_to_landlord_page',
          'nav_to_find_landlord_page',
          'set_search_results',
          'search_results'
        ],
  methods: {
    handle_search: function(event) {
      var search_str = event.target.search_box.value;
      console.log(search_str);
      $.post(search_landlords_url,
        {
          search_str: search_str
        },
        function(data) {
          console.log(data.landlords);
          this.set_search_results(data.landlords);
        }
      );
    },
    handle_property_select: function(event) {
      console.log(event);
    },
    handle_landlord_select: function(event) {
      console.log(event);
    }
  },
  template: `
    <div class="sub-page">
      <div class="search">
        <form @submit.prevent="handle_search" class="search-form">
          <input id="search_box" type="search" placeholder="Search for a Property"/>
          <button type="submit" id="search-button">
            <i class="fa fa-search"></i>
          </button>
        </form>
      <div>
      <div class="search-prompt">
        <p>
          didnt find what you are looking for?
          <a href="#" @click.prevent="nav_to_add_landlord">
            Find A Landlord
          </a>
        </p>
      </div>
    </div>

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
    props: ['toggle_selected_landlord',
            'create_landlord'],
    methods: {
      CreateLandlord_helper: function(event) {
          console.log(event);
          console.log(event.target.landlord_first_name.value);
          console.log(event.target.landlord_last_name.value);
          this.create_landlord(event);
          this.toggle_selected_landlord(event.target.landlord_first_name.value);
      }
    },
    template: `
      <div class="sub-page">
        <h1> Add New Landlord </h1>
        <form @submit.prevent="CreateLandlord_helper" class="add-landlord-form">

          <div class="landlord-form-item">
            <p>First Name</p>
            <input
              id="landlord_first_name"
              type="text" />
          </div>

          <div class="landlord-form-item">
            <p>Last Name</p>
            <input
              id="landlord_last_name"
              type="text" />
          </div>

          <div class="landlord-form-item">
            <p>Landlord's Website (Optional)</p>
            <input
              id="landlord_site"
              type="text" />
          </div>

          <div class="landlord-form-item">
            <button @v-on:click="CreateLandlord_helper" type="submit">
              <i class="fa fa-plus"></i>Confirm New Landlord
            </button>
          </div>
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

  self.nav_to_write_review = function() {
    self.vue.page = self.vue.WRITE_REVIEW;
  }

  self.toggle_selected_landlord = function(landlord_name) {
      console.log('youve made it thus far');
      self.vue.selected_landlord = landlord_name;
  }

  // API METHODS
  self.get_landlords = function() {
    $.getJSON(
      get_landlords_url,
      function(data){
        self.vue.landlord_list = data.landlords;
        console.log(self.vue.landlord_list);
      }
    );
  }

  self.create_landlord = function(event) {
    console.log(event);
    var form = event.target;
    var first_name = form.landlord_first_name.value;
    var last_name = form.landlord_last_name.value;
    var website = (form.landlord_site.value === "") ? "" : form.landord_site.value;
    $.post(
      create_landlord_url,
      {
        first_name: first_name,
        last_name: last_name,
        website: website,
      },
      function(data){
        console.log(data.landlord.first_name + " " + data.landlord.last_name + " was inserted into the database");
        self.vue.landlord_list.unshift(data.landlord);
      }
    );
  }

  self.set_search_results = function(results){
    self.vue.search_results = results;
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
      // ABOUT_PAGE: 7,
      // CONTACT_PAGE: 8,

      LANDLORD_TAGS: [
        'friendly',
        'mean',
        'chill',
        'understanding',
        'homie',
        'snoopy',
        'responsive',
        'lives nearby',
        'humorous',
        'will repair house'
      ],
      PROPERTY_TAGS: [
        'washer / dryer',
        'leaks',
        'old',
        'outdoor space',
        'spacious',
        'furnished',
        'utilities included',
        'good cell signal',
        'irritable neighbors',
        'sufficient parking'
      ],
      landlord_list: [],
      search_results: [],
      selected_landlord: 'Tom',
      form_title: null,
    },
    methods: {
      nav_to_find_landlord_to_review: self.nav_to_find_landlord_to_review,
      nav_to_find_landlord_page: self.nav_to_find_landlord_page,
      nav_to_find_property: self.nav_to_find_property,
      nav_to_create_landlord: self.nav_to_create_landlord,
      nav_to_home_page: self.nav_to_home_page,
      // nav_to_about_page: self.nav_to_about_page,
      // nav_to_contact_page: self.nav_to_contact_page,
      nav_to_landlord_page: self.nav_to_landlord_page,
      nav_to_write_review: self.nav_to_write_review,
      toggle_selected_landlord: self.toggle_selected_landlord,

      // APP FUNCTIONALITY
      create_landlord: self.create_landlord,
      set_search_results: self.set_search_results,
    }
  });

  self.get_landlords();
  $("#vue-div").show();
  return self;

};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});
