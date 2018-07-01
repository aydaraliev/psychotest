import {Component, DoCheck, OnInit} from '@angular/core';
import {Router} from '@angular/router';
import {LanguageService} from '../../services/language.service';
// declare var $: any;

@Component({
  selector: 'app-voted',
  templateUrl: './voted.component.html',
  styleUrls: ['./voted.component.scss'],
  providers: [LanguageService]
})

export class VotedComponent implements DoCheck, OnInit {
  firstName = '';
  secondName = '';
  birthday = '';
  matches = [];
  sended = false;
  voter = null;
  president = [];
  parlament = [];
  constructor(
    private langService: LanguageService,
    private router: Router
  ) { }

  ngOnInit() {
    // $('#birthday').datepicker([]);
  }

  ngDoCheck() {
    // const inputElement = <HTMLInputElement>document.getElementById('birthday');
    // this.birthday = inputElement.value;
  }

  findVoted (firstName: string, secondName: string, birthday: string): void {
    this.voter = null;
    this.matches = [];
    this.president = [];
    this.parlament = [];

    this.langService.findVoted(firstName, secondName, birthday)
      .subscribe(
        response => {
          this.sended = true;
          this.matches = response.matches;
          response.matches.map(item => {
            if (item.presidential) {
              this.president.push(item);
            } else {
              this.parlament.push(item);
            }
          });
        },
        error => {
          console.log(error);
          this.sended = true;
        }
      );
  }

  addLetter (letter: string, field: string): void {
    this[field] = this[field] + letter;
  }

  tagVoter (voter: Object): void {
    localStorage.setItem('voter', JSON.stringify(voter));
    localStorage.setItem('dob', JSON.stringify(this.birthday));
    this.foundNotFound(voter);
    this.router.navigate(['/feedback']);
  }

  foundNotFound (voter): void {
    this.langService.foundNotFound(voter).subscribe();
  }

  selectVoter (voter: Object): void {
    if (!this.voter) {
      this.voter = voter;
    } else {
      if (this.voter.presidential) {
        this.voter.parliamentary = true;
      } else {
        this.voter.presidential = true;
      }
    }
  }

  notFound (): void {
    localStorage.setItem('dob', JSON.stringify(this.birthday));
    const voter = {
      presidential: false,
      parliamentary: false
    };

    this.foundNotFound(voter);
    this.router.navigate(['/feedback']);
  }
}
