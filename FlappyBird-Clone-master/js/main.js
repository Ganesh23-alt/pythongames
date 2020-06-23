var canvas=document.getElementById("canvas");

var game=new Game(canvas);

var controller=new Controller();

var engine=new Engine(1000/30,update,render);

game.initializePipes();

game.loadAssets(engine);

function update(){
  game.update();
}

function render(){
  game.render();
}

window.addEventListener("keydown",function(event){
  controller.handleKeyDown(event);
});

window.addEventListener("keyup",function(event){
  controller.handleKeyDown(event);
});
