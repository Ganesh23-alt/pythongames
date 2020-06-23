class Bird{
  constructor(){
    this.x=150;
    this.y=250;
    this.jumping=false;
    this.jump_height=5;
    this.jump_timer=15;
    this.sprite=new Image();
    if(randomNumber(0,10)<=5){
      this.sprite.src='img/yellow.png';
    }else{
      this.sprite.src="img/blue.png";
    }
    this.height=24;
    this.width=34;
    this.sprite_counter=5;
    this.current_frame=1;
    this.jump_tick=this.jump_timer;
    this.color="red";
    this.angle=0;
    this.wing_sound= new Audio("resources/audio/wing.wav");
  }

  loadSprite(callback){
    this.sprite.addEventListener("load",function(){
      callback.start();
    })
  }

  fall(gravity){
    if(!this.jumping){
      this.y+=gravity;
      if(this.angle!=30){
        this.angle+=2;
      }
    }
  }

  jump(){
    this.wing_sound=this.wing_sound.cloneNode();
    this.wing_sound.play();
    this.jump_tick=this.jump_timer;
    if(!this.jumping){
      this.jumping=true;
    }
    if(this.jumping){
      this.y-=this.jump_height;
    }
  }

  tickJumpTimer(){
    if(this.jumping){
      if(this.jump_tick>0){
        this.angle=-30;
        this.y-=this.jump_height;
        this.jump_tick--;
      }else if(this.jump_tick==0){
        this.jump_tick=this.jump_timer;
        this.jumping=false;
      }
    }
    if(this.sprite_counter>0){
      this.sprite_counter--;
    }else if(this.sprite_counter==0){
      this.sprite_counter=5;
      if(this.current_frame>=2){
        this.current_frame=0;
      }else{
        this.current_frame++;
      }
    }
  }

  render(ctx){
    ctx.save();
    ctx.translate(Math.floor(this.x+(this.width/2)),Math.floor(this.y+(this.height/2)));
    ctx.rotate((this.angle)*Math.PI/180);
    ctx.drawImage(this.sprite,this.width*this.current_frame,0,this.width,this.height,-this.width/2.,-this.height/2,this.width,this.height);
    ctx.restore();
  }
}
