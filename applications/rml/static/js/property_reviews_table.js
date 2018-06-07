// this is the property page!

// notice our index.html has the tag <landlord></landlord>
//      that is were our code from this page is being rendered
//      notice in additon to the tag, at the bottom of our
//      our html page we render a script called
//      <script src="{{=URL('static', 'js/landlord.js')}}"></script>
//
// We will follow this form for future component development


// The property.js is how we will show a property page once a property
// is looked up and selected.  This is equivical to being on
// RateMyProfessors and reading Wesley Mackey's review.
//
// The Reviews are going to be implemented a table and within the table
// we will have pertient information

new Vue({
    el: 'property',
    template: `
        <div id="view">
            <h1>hello</h1>

            <table style="width:100%">
                <tbody>

                    <tr>
                        <th>Overall Rating</th>
                        <th>Break-Down</th>
                        <th>Comments</th>
                    </tr>
                        <tr>
                        <td>
                            <p>hello</p>
                        </td>
                        <td>
                            <p>hi</p>
                        </td>
                        <td>
                            <p>I will never rent with this property again</p>
                        </td>
                    </tr>

                    <tr>
                        <td>
                            <p>ello</p>
                        </td>
                        <td>
                            <p>i</p>
                        </td>
                    </tr>
                </tbody>
            </table>


            <button @click="showDescription">Description</button>
        </div>
    `,
});

