import { Injectable } from '@angular/core';
import { Socket } from 'ngx-socket-io';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root',
})

export class GameRoomService {

    userdata = {
        username: "randomUser",
        room: "chatroom1"
    }

    constructor(
        private socket: Socket, 
    ){}
    
    setUserDetails(username:string, room:string){
        this.userdata.username = username
    }

    async joinRoom(){
        this.socket.emit('join',this.userdata)
    }

    async leaveRoom(){
        this.socket.emit('leave',this.userdata)
    }

    async sendGuess(guess:string){
        let attrs = {
            "username": this.userdata.username,
            "room": this.userdata.room,
            "redirect_response": guess
        }
        this.socket.emit('auth_code',attrs)
        console.log("sent")
    }

    async sendGuess2(guess:string){
        let attrs = {
            "username": this.userdata.username,
            "room": this.userdata.room,
            "guess": guess
        }
        this.socket.emit('guess',attrs)
        console.log("sent")
    }

    listenForGuesses(): Observable<any> {
        return new Observable((observer) => {
            this.socket.on('message', (data: any) => {
                observer.next(data);
            });

            this.socket.on('auth_url', (data: any) => {
                window.open(data, '_blank');
            });
        });
    }
}

