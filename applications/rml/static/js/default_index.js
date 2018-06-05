// This is the js for the default/index.html view.

$(window).on("load", function() {
  $('.main-content').css('opacity', '1');
});

var app = function() {

  var self = {};

  Vue.config.silent = false; // show all warnings

  // Extends an array
  self.extend = function(a, b) {
      for (var i = 0; i < b.length; i++) {
          a.push(b[i]);
      }
  };

  // PROJECT SPECIFIC
  self.get_my_email = function(){
    $.getJSON(
      get_email_url,
      function(data){
        self.vue.logged_in = data.logged_in
        self.vue.current_user = data.current_user
      }
    );
  }

  self.get_memos = function() {
    // The URL is memo_list_url
    $.getJSON(
      memo_list_url,
      function(data){
        self.vue.memo_list = data.memos
        self.vue.are_publics = data.are_publics
        self.vue.are_privates = data.are_privates
      }
    );
  }

  self.form_toggle = function(){
    self.vue.is_creating = !self.vue.is_creating;
  }

  self.add_memo = function(){
    $.post(
      add_memo_url,
      {
        title: self.vue.form_title,
        body: self.vue.form_body,
        is_being_edited: false,
      },
      function(data){
        $.web2py.enableElement($("#add_memo_btn"));
        self.vue.memo_list.unshift(data.memo);
        self.vue.is_creating = false;
        self.vue.form_title = null;
        self.vue.form_body = null;
      }
    )
    self.vue.are_privates+=1;
  }

  self.delete_memo = function(memo_id) {
    $.post(
      del_memo_url,
      {
        memo_id: memo_id,
      },
      function () {
          var idx = null;
          for(var i = 0; i < self.vue.memo_list.length; i++){
            if (self.vue.memo_list[i].id === memo_id) {
              idx = i + 1;
              break;
            }
          }
          if(idx){
            self.vue.memo_list.splice(idx - 1, 1);
          }
          enumerate(self.vue.memo_list);
      }
    )
    self.vue.are_privates-=1;
  };

  self.edit_memo = function(memo_id, new_body_text, new_title_text){
    $.post(
      edit_memo_url,
      {
        memo_id: memo_id,
        body: new_body_text,
        title: new_title_text,
      },
      function () {
        for(var i = 0; i < self.vue.memo_list.length; i++){
          if (self.vue.memo_list[i].id === memo_id) {
            self.vue.memo_list[i].body = new_body_text;
            self.vue.memo_list[i].title = new_title_text;
            self.vue.memo_list[i].is_being_edited = false;
            break;
          }
        }
        enumerate(self.vue.memo_list);
      }
    )
  }

  self.edit_memo_btn = function(memo_id){
    for (var i = 0; i < self.vue.memo_list.length; i++){
      if(self.vue.memo_list[i].id === memo_id){
        self.vue.memo_list[i]['editor_body'] = self.vue.memo_list[i].body;
        self.vue.memo_list[i]['editor_title'] = self.vue.memo_list[i].title
        self.vue.memo_list[i].is_being_edited = true;
        break;
      }
    }
  }

  self.cancel_edit_memo_btn = function(memo_id){
    for (var i = 0; i < self.vue.memo_list.length; i++){
      if(self.vue.memo_list[i].id === memo_id){
        self.vue.memo_list[i].is_being_edited = false;
        break;
      }
    }
  }

  self.toggle_publicity = function(memo_id, setting){
    $.post(
      toggle_publicity_url,
      {
        memo_id: memo_id,
        is_public: setting,
      },
      function () {
        for(var i = 0; i < self.vue.memo_list.length; i++){
          if (self.vue.memo_list[i].id === memo_id) {
            self.vue.memo_list[i].is_public = setting;
            break;
          }
        }
        enumerate(self.vue.memo_list);
      }
    )
  }
  // -----------------

  // Complete as needed.
  self.vue = new Vue({
    el: "#vue-div",
    delimiters: ['${', '}'],
    unsafeDelimiters: ['!{', '}'],
    data: {
      memo_list: [],
      is_creating: false,
      form_title: null,
      form_body: null,
      current_user: null,
      are_publics: 0,
      are_privates: 0,
      logged_in: false,
    },
    methods: {
      form_toggle: self.form_toggle,
      add_memo: self.add_memo,
      delete_memo: self.delete_memo,
      edit_memo: self.edit_memo,
      edit_memo_btn: self.edit_memo_btn,
      cancel_edit_memo_btn: self.cancel_edit_memo_btn,
      toggle_publicity: self.toggle_publicity,
    }
  });

  self.get_my_email();
  self.get_memos();

  return self;

};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});
