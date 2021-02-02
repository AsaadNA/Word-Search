const generateColor = () => {
   color = []
   for(var i = 0; i <= 2; i++)
      color.push(Math.random() * (255 - 0) + 0)
   return color
}

const generateLetter = () => {
   var result = '';
   var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
   var charactersLength = characters.length;
   for ( var i = 0; i <= 0; i++ ) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
   } return result;
}

///

class Tile {

   constructor(x,y) {
      this.x = x;
      this.y = y;
      this.tileSize = 50;
      this.letterColor = generateColor()
      this.letterData = generateLetter()

      this.isMouseHovering = false
   }

   render() {
      rect(this.x, this.y, this.tileSize, this.tileSize);
      fill(this.letterColor[0],this.letterColor[1],this.letterColor[2])
      text(this.letterData,this.x+24,this.y+24)
      fill(255)
    }
}

///

class Board {

   constructor() {
      this.boardContainer = [];
      let xx = 0;
      let yy = 0;
      for(var i = 0; i <= 15; i++) {
         for(var j = 0; j <= 15; j++) {
            this.boardContainer.push(new Tile(xx,yy))
            xx += 50
         } xx = 0; yy += 50;
      } this.boardContainer.pop();
   }

   render() {
      background(0)
      this.boardContainer.forEach((letter) => {
         letter.render()
      })
   }
}

///

let board = new Board();

function setup() {
   createCanvas(750,750)
   textSize(35)
   textAlign(CENTER, CENTER);
}

function draw() {
   board.render();  
}