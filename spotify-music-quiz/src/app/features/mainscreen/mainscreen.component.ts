import { Component } from '@angular/core';

@Component({
  selector: 'Mainscreen',
  templateUrl: './mainscreen.component.html',
  styleUrl: './mainscreen.component.css'
})

export class MainscreenComponent {
  songPicture : string = '';
  answer : string = '';

  constructor() {}
}