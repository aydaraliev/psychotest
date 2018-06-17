import { Component, OnInit } from '@angular/core';
declare function require(path: string);

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss']
})
export class FooterComponent implements OnInit {
  imagePath = require('../../../../img/AUCA-Logo-2-tier-Left-COL22.png');

  constructor() { }

  ngOnInit() {
  }

}
