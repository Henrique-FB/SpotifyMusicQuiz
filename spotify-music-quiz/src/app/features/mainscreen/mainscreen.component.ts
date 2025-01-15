import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { GameRoomService } from '../../core/services/gameRoom.service';

@Component({
  standalone:true,
  imports: [FormsModule],
  selector: 'Mainscreen',
  templateUrl: './mainscreen.component.html',
  styleUrl: './mainscreen.component.css'
})

export class MainscreenComponent {
  songPicture : string = '';
  answer : string = '';

  constructor(private gameRoom:GameRoomService) {}

//  testFunc(){
//    this.gameRoom.joinRoom()
//  }


}