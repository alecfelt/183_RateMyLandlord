// this is the landlord page!

// notice our index.html has the tag <landlord></landlord>
//      that is were our code from this page is being rendered
//      notice in additon to the tag, at the bottom of our
//      our html page we render a script called
//      <script src="{{=URL('static', 'js/landlord.js')}}"></script>
//
// We will follow this form for future component development


// The landlord.js is how we will show a landlord page once a landlord
// is looked up and selected.  This is equivical to being on
// RateMyProfessors and reading Wesley Mackey's review.
//
// The Reviews are going to be implemented a table and within the table
// we will have pertient information

// see http://www.ratemyprofessors.com/ShowRatings.jsp?tid=2328264 for
// more information/inspiration  note, remove css if needed for easier viewing



// landlord tables review current just called landlord
// trs are reviews and td are sub fields of the reviews
//      note: the first 3tr are for the 3 tr headings
//      hence the indentations
new Vue({
    el: 'landlord-page',
    template: `
      <div class="sub-page">
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
  `,
});
