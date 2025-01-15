import { Injectable } from '@angular/core';
import { Socket } from 'ngx-socket-io';



@Injectable({
    providedIn: 'root',
})


export class GameRoomService {


    constructor(private socket: Socket) {}
    
    joinRoom(){
        this.socket.emit("join", "test")
    }

}

