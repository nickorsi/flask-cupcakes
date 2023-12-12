"use strict";

const $cupcakeList = $("#cupcake-list");
const $cupcakeForm = $("#create-cupcake-form");
const $submitButton = $("#cupcake-submit");

const BASE_URL = "localhost:5001"


function generateCupcakeMarkup(cupcake) {

  return $(`
      <li id="${cupcake.id}" class="cupcake-data">
        <img class="cupcake-image-url" src= ${cupcake.image_url} alt="Cupcake image">
        <small class="cupcake-flavor">Flavor: ${cupcake.flavor}</small>
        <small class="cupcake-size">Size: ${cupcake.size}</small>
        <small class="cupcake-rating">Rating: ${cupcake.rating}</small>
      </li>
    `);
}

function putCupcakesOnPage(cupcakes) {
  $cupcakeList.empty();

  for (let cupcake of cupcakes){
    const $cupcake = generateCupcakeMarkup(cupcake)

    $cupcakeList.append($cupcake);
  }
}



//Create event listener on create cupcake button
//create evnet listener on each cupcake to delete



/** Handle story form submission, if form has valid inputs - author, title, url,
 * and currentUser, it will call addStory and add it to the stories' list. */

// async function getAndSubmitCupcake(evt) {
//   console.debug("getStorySubmission=", evt);
//   evt.preventDefault();

//   const flavor = $("#flavor").val();
//   const size = $("#size").val();
//   const rating = $("#rating").val();
//   const url = $("#submit-url").val();

//   const currentCupcakes = await getCupcakes()

//   const $story = generateCupcakeMarkup(currentStory);
//   $allStoriesList.prepend($story);

// }

async function getCupcakes() {
    const response = await fetch(
      `/api/cupcakes`,
      {
        method: "GET"
      });

    const cupcakes = await response.json();

    return cupcakes;
}

async function start() {
  const cupcakes = await getCupcakes();
  putCupcakesOnPage(cupcakes.cupcakes);
}

start()

// $submitForm.on("submit", getAndSubmitStory);
