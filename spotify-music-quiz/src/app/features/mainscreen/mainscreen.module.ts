import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms'; // For ngModel
import { MainscreenComponent } from './mainscreen.component'; // Import the component

@NgModule({
  declarations: [
    MainscreenComponent,
  ],
  imports: [
    FormsModule // Import FormsModule for two-way binding
  ],
  bootstrap: [MainscreenComponent], // Define the root component to bootstrap
})

export class MainscreenModule {}