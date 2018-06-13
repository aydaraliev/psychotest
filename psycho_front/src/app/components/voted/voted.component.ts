import { Component } from '@angular/core';
import {Router} from "@angular/router";
import {LanguageService} from "../../services/language.service";

@Component({
  selector: 'app-voted',
  templateUrl: './voted.component.html',
  styleUrls: ['./voted.component.scss'],
  providers: [LanguageService]
})
export class VotedComponent {
  firstName = '';
  secondName = '';
  constructor(
    private langService: LanguageService,
    private router: Router
  ) { }

  findVoted (firstName: string, secondName: string) :void {
    this.langService.findVoted(firstName, secondName)
      .subscribe(
        response => {
          console.log(response);
        },
        error => console.log(error)
      );
  }
}
