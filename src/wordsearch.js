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
      this.letterColor = [0,0,0]
      this.letterData = generateLetter()
      this.filled = false;
   }

   isMouseInside(mouseX,mouseY) {
      return mouseX > this.x  && mouseX < this.x + this.tileSize && mouseY > this.y && mouseY < this.y + this.tileSize
   }

   setLetterColor(color) {
      this.letterColor = color
   }

   setFilled(data) {
      this.filled = data;
   }

   getFilled() {
      return this.filled;
   }

   getData() {
      return this.letterData;
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
      this.wordList = []
      this.wordLimit = 7

      let xx = 0;
      let yy = 0;
      for(var i = 0; i <= 15; i++) {
         for(var j = 0; j <= 15; j++) {
            this.boardContainer.push(new Tile(xx,yy))
            xx += 55
         } xx = 0; yy += 55;
      }
   }

   mouseReleased() {
      let completedWord = this.wordList.join();
      this.wordList = [];
      console.log("Completed Word: " + completedWord);
   }

   update(mouseX,mouseY,dragStatus) {
      if(this.wordList.length == 7) {
         dragStatus = false
      } else if(dragStatus == true) {
         this.boardContainer.forEach((letter) => {
         if(letter.isMouseInside(mouseX,mouseY) && letter.getFilled() == false) {
               letter.setFilled(true);
               letter.setLetterColor([255,0,0]);
               this.wordList.push(letter.getData()) 
            }
         })
      }
   }

   render() {
      this.boardContainer.forEach((letter) => {
         letter.render()
      })
   }
}

///

let board = new Board();
let mouseDrag = false;

function setup() {
   createCanvas(823,823)
   textSize(35)
   textAlign(CENTER, CENTER);
   cursor(CROSS);
}

function mousePressed() {
   mouseDrag = true;
}

function mouseReleased() {
   mouseDrag = false;
   board.mouseReleased();
}

function mouseDragged() {
   if(mouseDrag) board.update(mouseX,mouseY,mouseDrag)
}

function draw() {
   board.render();  
}