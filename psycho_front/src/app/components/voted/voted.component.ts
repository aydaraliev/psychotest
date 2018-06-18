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
  birthday = '';
  matches = [];
  sended = false;
  voter = null;
  constructor(
    private langService: LanguageService,
    private router: Router
  ) { }

  findVoted (firstName: string, secondName: string, birthday: string) :void {
    this.langService.findVoted(firstName, secondName, birthday)
      .subscribe(
        response => {
          this.sended = true;
          this.matches = response.matches;
        },
        error => {
          console.log(error);
          this.sended = true;
        }
      );
  };

  addLetter (letter: string, field: string) :void {
    this[field] = this[field] + letter;
  }

  tagVoter (voter: Object) :void {
    localStorage.setItem('voter', JSON.stringify(voter));
    this.router.navigate(['/feedback']);
  };
}
