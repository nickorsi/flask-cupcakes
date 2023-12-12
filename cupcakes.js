"use strict";

const $cupcakeList = $("#cupcake-list");
const $cupcakeForm = $("#create-cupcake-form");
const $submitButton = $("#cupcake-submit");


//Want a function that renders HTML

    return jsonify(cupcakes=serialized)

function generateCupcakeMarkup(cupcake) {

  return $(`
      <li id="${story.id}" class="cupcake-data">
        <small class="cupcake-image-url"> ${cupcake.image_url} </small>
        <small class="cupcake-flavor">Flavor:(${cupcake.flavor})</small>
        <small class="cupcake-size">Size::${cupcake.size}</small>
        <small class="cupcake-rating">Rating:${cupcake.rating}</small>
      </li>
    `);
}

function putCupcakesOnPage() {
  $cupcakeList.empty();

  for (let cupcake of /**[???]**/){
    const $cupcake = generateCupcakeMarkup(cupcake)

    $cupcakeList.append($cupcake);
  }
}



//Create event listener on create cupcake button
//create evnet listener on each cupcake to delete



/** Handle story form submission, if form has valid inputs - author, title, url,
 * and currentUser, it will call addStory and add it to the stories' list. */

async function getAndSubmitCupcake(evt) {
  console.debug("getStorySubmission=", evt);
  evt.preventDefault();

  const flavor = $("#flavor").val();
  const size = $("#size").val();
  const rating = $("#rating").val();
  const url = $("#submit-url").val();

  // grab current user
  console.log("whatIsUser=", currentUser);
  console.log("currentStory=", currentUser, { title, author, url });

  const currentStory = await storyList.addStory(
    currentUser,
    { title, author, url }
  );
  const $story = generateStoryMarkup(currentStory);
  $allStoriesList.prepend($story);

  $submitForm.trigger("reset");
  $submitForm.fadeOut("slow");
}

$submitForm.on("submit", getAndSubmitStory);
