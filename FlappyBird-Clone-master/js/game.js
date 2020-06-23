class Game{
  constructor(canvas){
    this.score=0;
    this.canvas=canvas;
    this.bird=new Bird();
    this.pipes=[];
    this.gravity=5;
    this.pipe_speed=0;
    this.pipe_number=3;
    this.pipe_start=500;
    this.pipe_distance=200;
    this.background_pattern=undefined;
    this.ctx=this.canvas.getContext('2d');
    this.floor_pattern=undefined;
    this.latest_pipe=this.pipe_number-1;
    this.game_over=false;
    this.canvas_width=450;
    this.screen=0;
		this.canvas_height=600;
    this.game_start=false;
  }

  loadAssets(callback){
    this.floor=new Image();
    this.background=new Image();
    this.game_over_sprite=new Image();
    this.ready_sprite=new Image();
    this.ready_sprite.src="img/ready.png";
    this.floor.src="img/base.png";
    this.background.src="img/background.png";
    this.game_over_sprite.src='img/gameover.png';
    this.hit_sound= new Audio("resources/audio/hit.wav");
    this.point_sound= new Audio("resources/audio/point.wav");
    this.assets=[this.floor,this.background,this.game_over_sprite,this.ready_sprite,this.hit_sound,this.point_sound];

    this.assets.forEach(function(asset,index){
      asset.addEventListener("load",function(){
        callback.start();
      })
    })
    this.bird.loadSprite(callback);
  }


  initializePipes(){
    for(var i=0;i<this.pipe_number;i++){
      this.pipes.push(new Pipe(this.pipe_start+i*this.pipe_distance));
    }
  }

  movePipes(){
    this.pipes.forEach(function(pipe,index){
      pipe.move(this.pipe_speed);
      if(pipe.x<=(-pipe.pipe_width)){
        if(index==0){
          this.latest_pipe=2;
        }else{
          this.latest_pipe=index-1;
        }
        pipe.x=this.pipes[this.latest_pipe].x+this.pipe_distance;
      }
    }.bind(this))
  }

  bird_fall(){
    if((this.bird.y+this.bird.height)<this.canvas_height){
      this.bird.fall(this.gravity);
    }
  }

  bird_jump(){
    this.bird.jump();
  }

  checkCollision(){
      this.pipes.forEach(function(pipe,index){
        if(this.bird.x<=(pipe.x+pipe.pipe_width) && (this.bird.x+this.bird.width)>=pipe.x && (this.bird.y<=pipe.top || (this.bird.y+this.bird.height)>=pipe.bottom)){
          this.game_over=true;
          this.hit_sound.play();
        }
        if(((pipe.x+pipe.pipe_width)-this.bird.x)<this.pipe_speed && ((pipe.x+pipe.pipe_width)-this.bird.x)>0){
          this.score++;
          this.point_sound.play();
        }
      }.bind(this));

      if((this.bird.y+this.bird.height)>(this.canvas_height-this.floor.height)){
        this.game_over=true;
        this.hit_sound.play();
      };
    }

  checkDead(){
    if(this.game_over){
      this.screen=2;
      engine.stop();
      engine.run();
    }
  }

  showGameOver(){
    this.ctx.drawImage(this.game_over_sprite,0,0,this.game_over_sprite.width,this.game_over_sprite.height,140,150,this.game_over_sprite.width,this.game_over_sprite.height);
  }

  showReady(){
    this.ctx.drawImage(this.ready_sprite,0,0,this.ready_sprite.width,this.ready_sprite.height,140,150,this.ready_sprite.width,this.ready_sprite.height);
  }

  update(){
    if(this.game_start){
      this.bird_fall();
    }
    this.bird.tickJumpTimer();
    this.movePipes();
    this.checkCollision();
    this.checkDead();
  }

  renderPipes(){
    this.pipes.forEach(function(pipe,index){
      pipe.render(this.ctx);
    }.bind(this))
  }

  renderBackground(){
    this.background_pattern=this.ctx.createPattern(this.background,'repeat-x');;
    this.ctx.save();
    this.ctx.fillStyle=this.background_pattern;
    this.ctx.translate(0,0);
    this.ctx.fillRect(0,0,this.canvas_width,this.canvas_height-this.floor.height);
    this.ctx.restore();
  }

  renderFloor(){
    this.floor_pattern=this.ctx.createPattern(this.floor,"repeat-x");
    this.ctx.save();
    this.ctx.fillStyle = this.floor_pattern;
    this.ctx.translate(0, this.background.height-25);
    this.ctx.fillRect(0, 0, this.canvas_width, this.floor.height);
    this.ctx.restore();
  }

  renderStatus(){
    this.ctx.font=("25px Verdana");
    this.ctx.fillText("Score : " + this.score,260,30);
  }

  render(){
    this.ctx.clearRect(0,0,this.canvas_width,this.canvas_height);
    this.renderBackground();
    this.renderPipes();
    this.renderFloor();
    this.bird.render(this.ctx);
    this.renderStatus();
  }

}
