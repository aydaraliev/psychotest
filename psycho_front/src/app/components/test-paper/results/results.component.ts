import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.scss']
})
export class ResultsComponent {
  isToggle = false;

  @Input() extraversion: number;
  @Input() neuroticism: number;
  @Input() openness: number;
  @Input() consciousness: number;
  @Input() friendly: number;

  constructor() { }

  toggleResults(): void {
    console.log(1);
    this.isToggle = !this.isToggle;
  }

}
