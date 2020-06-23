class Pipe{
  constructor(x){
    this.pipe_gap=160;
    this.x=x;
    this.pipe_width=55;
    this.pipe_height=242;
    this.top=randomNumber(100,240);
    this.bottom=this.top+this.pipe_gap;
    this.top_sprite=new Image();
    this.bottom_sprite=new Image();
    this.top_sprite.src='img/top.png';
    this.bottom_sprite.src="img/bottom.png";
  }

  render(ctx){
    ctx.drawImage(this.top_sprite,0,0,this.pipe_width,this.pipe_height,this.x,this.top-this.pipe_height,this.pipe_width,this.pipe_height)
    ctx.drawImage(this.bottom_sprite,0,0,this.pipe_width,this.pipe_height,this.x,this.bottom,this.pipe_width,this.pipe_height)
  }

  move(speed){
    this.x-=speed;
  }

}
