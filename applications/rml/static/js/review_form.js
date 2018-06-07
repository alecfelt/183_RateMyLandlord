// review_form.js






// here lies the old entire index.html page or at least the one that existed in
// the branch viewForm and any others that agreed with it.  The purpose of having
// it here is solely it attempt to extract the form that exists and have it
// extracted as a component.










// {{extend 'layout.html'}}

// {{block head}}
// <script src="{{=URL('static', 'js/vue.js')}}"></script>
// <script>
//   var memo_list_url = "{{=URL('api', 'get_memos')}}";
//   var add_memo_url = "{{=URL('api', 'add_memo', user_signature=True)}}";
//   var del_memo_url = "{{=URL('api', 'del_memo', user_signature=True)}}";
//   var edit_memo_url = "{{=URL('api', 'edit_memo', user_signature=True)}}"
//   var toggle_publicity_url = "{{=URL('api', 'toggle_publicity', user_signature=True)}}"
//   var get_email_url = "{{=URL('api', 'get_my_email', user_signature=True)}}"
//   var add_review_url = "{{ =URL('api', 'add_review', user_signature=True) }}"
// </script>
// {{end}}



// <div class="main_content">
//   <div class="app_content">
//     <div id="vue-div" v-cloak>
//       <transition name="fade">
//       <div v-if="logged_in">
//         <p v-if="!are_privates && !is_creating">Please use the add new memo button to create your first memo!</p>
//         <p v-if="!are_privates && is_creating">Great! Now fill out this form with your first memo and hit the "Post This Memo" button to post it. Or you can cancel below.</p>
//         <button v-if="!is_creating"
//                 v-on:click="form_toggle()"
//                 id="add_new_memo_btn"
//                 class="btn">
//           <i class="fa fa-plus"></i> Add New Memo
//         </button>
//         <button v-if="is_creating" class="btn"  id="add_new_memo_btn" v-on:click="form_toggle()">
//           <i class="fa fa-times fa-lg"></i> Cancel
//         </button>

//         <!-- <div v-if="is_creating" id="new_memo"> -->
//         <!--   <p class="memo_title">New Memo</p> -->
//         <!--   <form action="#" v-on:submit.prevent="add_memo" class="form-horizontal"> -->
//         <!--     <div class="form-group" id="memo_title_input"> -->
//         <!--       <div> -->
//         <!--         <input placeholder="Memo Title" v-model="form_title" name="title" type="text" /> -->
//         <!--       </div> -->
//         <!--     </div> -->
//         <!--     <div class="form-group" id="memo_body_input"> -->
//         <!--       <div> -->
//         <!--         <input placeholder="Memo Content" v-model="form_body" name="body" type="text" /> -->
//         <!--       </div> -->
//         <!--     </div> -->
//         <!--     <div class="new_memo_buttons"> -->
//         <!--       <div class="form-group" id="submit_memo"> -->
//         <!--         <div> -->
//         <!--           <input class="btn btn-primary " id="add_memo_btn" type="submit" value="Post This Memo" /> -->
//         <!--         </div> -->
//         <!--       </div> -->
//         <!--     </div> -->
//         <!--   </form> -->
//         <!-- </div> -->

//         <div v-if="is_creating" id="new_memo">
//           <p class="memo_title">New Memo</p>
//           <form action="#" v-on:submit.prevent="add_review" class="form-horizontal">

//             <div>
//               <input
//                 placeholder="Memo Title: left these the same for now"
//                 v-model="form_title"
//                 name="title"
//                 type="text" />
//             </div>

//             <div>
//               <input
//                 placeholder="Memo Content"
//                 v-model="form_body"
//                 name="body"
//                 type="text" />
//             </div>

//             <div>
//                 <p> Rate your landlord </p>
//                 <select v-model="form_landlord_rating">
//                     <option selected="true" disabled="true">
//                         please select
//                     </option>
//                     <option value="1"> 1 </option>
//                     <option value="2"> 2 </option>
//                     <option value="3"> 3 </option>
//                     <option value="4"> 4 </option>
//                     <option value="5"> 5 </option>
//                 </select>
//             </div>

//             <div>
//                 <p> Rate your property </p>
//                 <select v-model="form_property_rating">
//                     <option selected="true" disabled="true">
//                         please select
//                     </option>
//                     <option value="1"> 1 </option>
//                     <option value="2"> 2 </option>
//                     <option value="3"> 3 </option>
//                     <option value="4"> 4 </option>
//                     <option value="5"> 5 </option>
//                 </select>
//             </div>

//             <div>
//                 <p> is this a landlord or a land management group </p>
//                 <select v-model="form_is_landlord">
//                     <option value="landlord"> landlord </option>
//                     <option value="group/org/ect"> group/org/ect </option>
//                 </select>
//             </div>

//             <div>
//                 <p> How would you rate your landlord's responsiveness? </p>
//                 <div>
//                    <select v-model="form_responsiveness">
//                         <option selected="true" disabled="true">
//                             perhaps we can fill this with fun descriptive words
//                             similar to RMP
//                         </option>
//                         <option value="1"> 1 </option>
//                         <option value="2"> 2 </option>
//                         <option value="3"> 3 </option>
//                         <option value="4"> 4 </option>
//                         <option value="5"> 5 </option>
//                     </select>
//                 </div>
//             </div>

//             <div>
//                 <p> Would you rent with this landlord again?<p>
//                 <div>
//                     <input type="radio" name="land" value="yes" v-model="form_rent_landlord_again">yes!<br>
//                     <input type="radio" name="land" value="no" v-model="form_rent_landlord_again">no!<br>
//                 </div>
//             </div>

//             <div>
//                 <p> Would you rent this propery again? </p>
//                 <div>
//                     <input type="radio" name="rent" value="yes">yes!<br>
//                     <input type="radio" name="rent" value="no">no!<br>
//                 </div>
//             </div>

//             <div>
//                 <p> chill? </p>
//                 <div>
//                     <input type="radio" name="chill"> yas <br>
//                     <input type="radio" name="chill"> yesn't <br>
//                 </div>
//             </div>

//             <div>
//                 <p>
//                     please select from a list of tags that you think you'd find helpful
//                     perhaps this could also take in user #hashtags or something cool.
//                 </p>
//                 <div>
//                     <ul>
//                         <li>pets allowed</li>
//                         <li>show up unannounced</li>
//                         <li>lives far away</li>
//                         <li>accepts venmo</li>
//                         <li>. . . if this list goes longer the footer covers sumbit button</li>
//                         <li>write your own?</li>
//                     </ul>
//                 </div>
//             </div>

//             <div>
//                 <p> Your unique experience </p>
//                 <textarea v-model="form_review_body">

//                 </textarea>
//             </div>

//             <div class="new_memo_buttons">
//               <div class="form-group" id="submit_memo">
//                 <div>
//                   <input class="btn btn-primary " id="add_memo_btn" type="submit" value="Post This Memo" />
//                 </div>
//               </div>
//             </div>
//           </form>
//         </div>
//         <!-- end of form -->

//         <!-- form in static/js/landlord for displaying reviews of landlord -->
//         <landlord></landlord>

//         <!-- this is the property compenet: -->
//         <!-- if uncommented, it will display the table -->
//         <!-- <propery></propery> -->

//         <h3 v-if="are_privates">Your Memos</h3>
//         <div class="memo_list">
//           <div v-for="memo in memo_list">
//             <div v-if="current_user === memo.user_email" class="memo">
//               <p v-if="!memo.is_being_edited" class="memo_title">${memo.title}</p>
//               <p v-if="!memo.is_being_edited">${memo.body}</p>
//               <div v-if="memo.is_being_edited" class="memo_editor">
//                 <form action="#" v-on:submit.prevent="edit_memo(memo.id, memo.editor_body, memo.editor_title)" class="form-horizontal">
//                   <div class="form-group" id="memo_title_input">
//                     <div>
//                       <input placeholder="Memo Title" v-model="memo.editor_title" name="title" type="text" />
//                     </div>
//                   </div>
//                   <div class="form-group" id="memo_body_input">
//                     <div>
//                       <input placeholder="Memo Content" v-model="memo.editor_body" name="body" type="text" />
//                     </div>
//                   </div>
//                 </form>
//               </div>
//               <div v-if="memo.is_being_edited" class="editor button_list">
//                 <button class="btn " v-on:click="edit_memo(memo.id, memo.editor_body, memo.editor_title)" href="">
//                   <i class="fa fa-save fa-lg"></i>
//                 </button>
//                 <button v-on:click="cancel_edit_memo_btn(memo.id)" class="btn " href="">
//                   <i class="fa fa-times fa-lg"></i>
//                 </button>
//               </div>
//               <div v-if="!memo.is_being_edited" class="static button_list">
//                 <button v-if="memo.is_public" v-on:click="toggle_publicity(memo.id, false)" class="btn " href="">
//                   <i class="fa fa-users"></i>
//                 </button>
//                 <button v-if="!memo.is_public" v-on:click="toggle_publicity(memo.id, true)" class="btn " href="">
//                   <i class="fa fa-user"></i>
//                 </button>
//                 <button v-on:click="edit_memo_btn(memo.id)" class="btn " href="">
//                   <i class="fa fa-edit fa-lg"></i>
//                 </button>

//                 <!-- Button to Delete  -->
//                 <button v-on:click="delete_memo(memo.id)"
//                         class="btn ">
//                   <i class="fa fa-trash fa-lg"></i>
//                 </button>
//               </div>
//             </div>
//           </div>
//         </div>

//       <h3 v-if="are_publics">Public Memos</h3>
//       <div class="memo_list">
//         <div v-for="memo in memo_list">
//           <div v-if="(current_user !== memo.user_email) && memo.is_public === true" class="memo">
//             <p class="memo_title">${memo.title}</p>
//             <p>${memo.body}</p>
//           </div>
//         </div>
//       </div>

//     </div>
//     </transition>
//     <div v-if="!logged_in">

//       <h1 class="main_title">Welcome!</h1>
//       <p class="explanation">This site will allow you to post and react to reviews of local landlords. You can view all public reviews without an account, but in order to edit your reviews and interact with the community, you will need to create one and log in.</p>
//       <div class="login_button">
//         <a href="{{=URL('default', 'user')}}" class="btn rounded">Login / Sign Up</a>
//       </div>

//       <div class="initial-prompt">
//         <h2>Find what you are looking for:</h2>
//         <div class="center_button_list">
//           <a href="{{=URL('default', 'user')}}" class="btn rounded">Find a <b>Landlord</b></a>
//           <a href="{{=URL('default', 'user')}}" class="btn rounded">Find a <b>House</b></a>
//           <a href="{{=URL('default', 'user')}}" class="btn rounded">Write a <b>Review</b></a>
//         </div>
//       </div>

//     </div>
//   </div>
//   </div>
// </div>

// <script src="{{=URL('static', 'js/default_index.js')}}"></script>
// <script src="{{=URL('static', 'js/landlord.js')}}"></script>
// <script src="{{=URL('static', 'js/property.js')}}"></script>
