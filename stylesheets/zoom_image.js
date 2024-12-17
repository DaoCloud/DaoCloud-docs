window.onload = function () {
  for (let item of document.getElementsByTagName("img")) {
    if (item.classList.contains("pass") === false) {
      item.setAttribute("onclick", "clickAction(this)");
    }
  }
};

function clickAction(img) {
  let medusa = document.createElement("div");
  medusa.setAttribute("id", "imgBaseDiv");
  medusa.setAttribute("onclick", "closeImg()");
  let image = document.createElement("img");
  image.setAttribute("src", img.src);
  medusa.appendChild(image);
  document.body.appendChild(medusa);
}

function closeImg() {
  document.getElementById("imgBaseDiv").remove();
}
