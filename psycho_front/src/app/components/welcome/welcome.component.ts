import {Component, DoCheck, OnInit} from '@angular/core';
import { LanguageService } from '../../services/language.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.scss'],
  providers: [LanguageService]
})
export class WelcomeComponent implements DoCheck, OnInit {
  lang = 0;

  constructor(
    private langService: LanguageService,
    private router: Router
  ) {}

  onSelectLang(lang: number) {
    this.langService.changeLanguage(lang);
    this.router.navigate(['/privacy']);
  }

  ngDoCheck() {
    this.lang = Number(localStorage.lang);
  }

  ngOnInit() {
    localStorage.removeItem('text-results');
    localStorage.removeItem('results');
  }

}
