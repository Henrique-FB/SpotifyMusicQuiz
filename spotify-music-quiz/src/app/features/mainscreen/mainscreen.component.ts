import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { GameRoomService } from '../../core/services/gameRoom.service';
import { Socket } from 'ngx-socket-io';


@Component({
  standalone:true,
  imports: [FormsModule],
  selector: 'Mainscreen',
  templateUrl: './mainscreen.component.html',
  styleUrl: './mainscreen.component.css'
})

export class MainscreenComponent {
  songPicture : string = '';
  guess : string = '';
  username : string = "randomUser"

  testComms : string = '';


  constructor(private gameRoom:GameRoomService) {}

  ngOnInit() {
    const params = new URLSearchParams(window.location.search);
    const authCode = params.get('code');
    console.log(authCode)
    if(authCode){
    this.gameRoom.setUserDetails(this.username,'chatroom1',authCode);
    this.gameRoom.joinRoom()
    }
    
    if(!authCode){
      this.gameRoom.setUserDetails(this.username,'chatroom1','');
      this.gameRoom.joinRoom();
    }


    this.gameRoom.listenForGuesses().subscribe((data)=>{
      this.testComms = data
      console.log(data)
    });

  }
  
  sendGuess(){
    this.gameRoom.sendGuess(this.guess);
    console.log("sent")
  }
}