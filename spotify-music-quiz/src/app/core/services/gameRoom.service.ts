import { Injectable } from '@angular/core';
import { Socket } from 'ngx-socket-io';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root',
})

export class GameRoomService {

    userdata = {
        username: "randomUser",
        room: "chatroom1",
        authCode: "",
    }

    constructor(
        private socket: Socket, 
    ){}
    
    setUserDetails(username:string, room:string, authCode:string){
        this.userdata.username = username
        this.userdata.authCode = authCode
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
                window.location.href = data;
            });
        });
    }
}

