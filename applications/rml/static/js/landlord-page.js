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
        <div id="view">

            <table style="width:100%">
                <tbody>

                    <tr>
                        <th>Overall Rating</th>
                        <th>Break-Down</th>
                        <th>Comments</th>
                    </tr>

                    <tr>
                        <td>
                            <p> date?? rmp has this and it could be relevant </p>
                            <p> overall landlord rating 1-5 </p>
                            <p> overall property rating 1-5 if applicable</p>
                        </td>

                        <td>
                            <p><a href="">
                                address if provided, link to property page
                            </a></p>
                            <p> responsiveness score </p>
                            <p> chill? </p>
                        </td>

                        <td>
                            <span> tag box, rmp puts the tags in this collumn as spans on top </span>
                            <span> showed unannounced </span>
                            <span> accepts venmo </span>
                            <p>
                                big ass lorem ipsum comment review block for users response
                            </p>
                            <p>
                                bottom line: yes/no would rate with ll again
                            <p>
                        </td>

                    </tr>
                </tbody>
            </table>


        </div>
    `,
});

