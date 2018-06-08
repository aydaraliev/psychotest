import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { HeaderComponent } from './components/common/header/header.component';
import { FooterComponent } from './components/common/footer/footer.component';
import { AppRoutingModule } from './app-routing/app-routing.module';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { TestPaperComponent } from './components/test-paper/test-paper.component';
import { ProgressComponent } from './components/test-paper/progress/progress.component';
import { ResultsComponent } from './components/test-paper/results/results.component';
import { TestListComponent } from './components/test-list/test-list.component';
import { TermsComponent } from './components/common/terms/terms.component';
import { PrivacyComponent } from './components/common/privacy/privacy.component';
import { FormFeedbackComponent } from './components/form-feedback/form-feedback.component';
import { TestResultsComponent } from './components/test-results/test-results.component';
import { WelcomeComponent } from './components/welcome/welcome.component';
import { VotedComponent } from './components/voted/voted.component';


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    TestPaperComponent,
    ProgressComponent,
    ResultsComponent,
    TestListComponent,
    TermsComponent,
    PrivacyComponent,
    FormFeedbackComponent,
    TestResultsComponent,
    WelcomeComponent,
    VotedComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
