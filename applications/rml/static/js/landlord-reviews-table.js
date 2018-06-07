// this is the landlord-page-tables.js page
// still not the proper implementation but it
// is the just a skeleton to reference/stylize
// then port over


// landlord tables review current just called landlord
// trs are reviews and td are sub fields of the reviews
//      note: the first 3tr are for the 3 tr headings
//      hence the indentations

new Vue({
    el: 'landlord-reviews-table',
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

                    <br>
                    <br>
                    Line breaks for readability
                    <br>
                    <br>

                    <tr>
                        <td>
                            <p> date?? 11/2/18 </p>
                            <p> 4 </p>
                            <p></p>
                        </td>

                        <td>
                            <p><a href="">
                                420 high St
                            </a></p>
                            <p> Very Responsive </p>
                            <p> chill? yee </p>
                        </td>

                        <td>
                            <span> lives far </span>
                            <span> accepts venmo </span>
                            <p>
                                Greg is the bes, the rent is cheap and he even let my housemate
                                keep a pet hedgehog in the house.  The only downside I guess is
                                That Greg absolutely stressed that we could not have subletters,
                                a bit of a bummer since I went away for summer and had to get
                                a little sneaky with letting my friend stay in.  All in all a
                                pretty chill set up and Greg is fine with students.  EXPENSIVE
                                though but what did you expect?

                            </p>
                            <p>
                                bottom line: yes I would rent with Greg again
                            <p>
                        </td>
                    </tr>



                </tbody>
            </table>


        </div>
    `,
});

