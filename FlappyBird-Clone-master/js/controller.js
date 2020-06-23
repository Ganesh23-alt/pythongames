
class Controller{
  constructor(){
    this.keydown=false;
  }

  handleKeyDown(event){
    if(event.type=="keydown" && !this.keydown){
      if(event.keyCode==32 && !game.game_start){
        game.game_over=false;
        game.game_start=true;
        game.pipe_speed=2;
        game.screen=1;
        engine.run();
      }else if(event.keyCode==32 && game.game_over){
        game=new Game(canvas);
        game.loadAssets(engine);
        game.initializePipes();
        game.screen=0;
        game.pipe_speed=0;
        engine.run();
      }
      if(event.keyCode==32){
        game.bird_jump();
        this.keydown=true;
      }
    }else if(event.type=="keyup" && this.keydown){
      this.keydown=false;
    }
  }
}
