"use strict";

const $cupcakeList = $("#cupcake-list");
const $cupcakeForm = $("#create-cupcake-form");

const BASE_URL = "localhost:5001"


/** Given a cupcake, creates markup to be appended to DOM.
 *
 * A cupcake is {id, flavor, size, rating, image-url}
 * */

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

/** Given list of cupcakes, create markup for each and appends to DOM by
 *  populating #cupcakesList. Clears cupcake list first
 *
 * A cupcake is {id, flavor, size, rating, image-url}
 * */

function putCupcakesOnPage(cupcakes) {
  $cupcakeList.empty();

  for (let cupcake of cupcakes){
    const $cupcake = generateCupcakeMarkup(cupcake)

    $cupcakeList.append($cupcake);
  }
}

/** Queries a GET request to API and returns (promise) array of cupcake objects
 *
 * Returns (promise): {cupcakes: [{id, flavor, size, rating, image_url}, ...]}.
 */

async function getCupcakes() {
  //TODO:Why we don't need Base
  const response = await fetch(
    `/api/cupcakes`,
    {
      method: "GET"
    });

  const cupcakes = await response.json();

  return cupcakes;
}

/** Handle cupcake form submission, if form has valid inputs - flavor, rating,
 * size, image-url, it will POST cupcake and add it to the cupcakes' list. */

async function getAndSubmitCupcake(evt) {
  evt.preventDefault();

  const flavor = $("#flavor").val();
  const size = $("#size").val();
  const rating = $("#rating").val();
  const image_url = $("#submit-url").val();

  console.log("HERE")

  const response = await fetch(
    `/api/cupcakes`,
    {
      method: "POST",
      body: JSON.stringify({flavor:flavor, size:size, rating:rating,
         image_url:image_url}),
      headers: {"Content-Type":  "application/json"},
    });

  console.log("NOT HERE")

  const newCupcake = await response.json();

  const $cupcake = generateStoryMarkup(newCupcake.cupcake);
  $cupcakeList.prepend($cupcake);
}


// Once form is submitted, calls getAndSubmitCupcake to POST to API and append
// to DOM

$cupcakeForm.on("submit", getAndSubmitCupcake);


/** Starts the homepage and calls getCupcake to populate the DOM */

async function start() {
  const cupcakes = await getCupcakes();
  putCupcakesOnPage(cupcakes.cupcakes);
}

start()


