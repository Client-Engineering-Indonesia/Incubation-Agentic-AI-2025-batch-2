import logo from './logo.svg';
import './App.css';
import './_landing-page.scss';

import { Grid, Column } from '@carbon/react';

import Header from './images/HeaderLong.png';
import React, { useState, useEffect } from 'react';
import OpeningIllustrationOpen from './images/OpeningIllustrationOpen.png';

function App() {
  const isSidebarOpen = false;

  const [lgValue1, setLgValue1] = useState(isSidebarOpen ? 4 : 5);
  const [lgValue2, setLgValue2] = useState(isSidebarOpen ? 5 : 6);
  const [imgWidth, setImgWidth] = useState(isSidebarOpen ? 275 : 189);
  const [imgHeight, setImgHeight] = useState(isSidebarOpen ? 242 : 167);
  const [imgColumn, setImgColumn] = useState(isSidebarOpen ? 4 : 3);
  const [textColumn, setTextColumn] = useState(isSidebarOpen ? 7 : 11);

  useEffect(() => {
    setLgValue1(isSidebarOpen ? 4 : 5);
    setLgValue2(isSidebarOpen ? 5 : 6);
    setImgWidth(isSidebarOpen ? 275 : 189);
    setImgHeight(isSidebarOpen ? 242 : 167);
    setImgColumn(isSidebarOpen ? 4 : 3);
    setTextColumn(isSidebarOpen ? 7 : 11);
    
  }, [isSidebarOpen]);

  
  return (
    <div style={{background: 'white'}}>
      <div style={{ position: 'relative', maxWidth: '100%' }}>
        
        <img src={Header} style={{ width: '100%', height: 300 }} />
        <div
          style={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            textAlign: 'center',
            color: '#fff',
          }}
        >
          <h2 style={{ fontSize: '18px', fontWeight: 500 }}>
            IBM{' '}
            <span style={{ fontSize: '18px', fontWeight: 700 }}>watsonx</span>
          </h2>
          <br></br>
          <h2 style={{ fontSize: '36px', fontWeight: 700 }}>
            Agentic AI Workshop
          </h2>
        </div>
      </div>
      <div style={{ height: '100vh' }}>
        <div style={{ height: '100vh' }}>
        <div>
          <div className="text-container" style={{
            marginLeft: isSidebarOpen ? '1rem' : '0',
            transition: 'margin-left 0.3s ease',
            padding: '1rem 5rem'
          }}>
            
            <p className="description" >
            Agentic AI represents a leap beyond traditional generative models: it comprises autonomous agents that plan, decide, and act toward goals with minimal human oversight. Each agent tackles a specific subtask—from gathering data to taking actions—while orchestration layers ensure seamless collaboration. This architecture enables systems that are autonomous, goal-driven, and remarkably adaptive.
Why IBM? IBM brings this vision to life through its watsonx Orchestrate platform, which integrates orchestration, governance, and hybrid-cloud flexibility—letting your business build, deploy, and manage autonomous agents securely, across complex environments . Ready to see AI that truly acts?
<br></br><br></br>
On July 16, 2025, IBM inaugurated its Agentic AI Innovation Center in Bengaluru—a co‑creation hub where enterprises, developers, startups, and partners collaborate to design, test, and deploy real-world AI agents at scale.
Inside, you'll find hands-on labs powered by watsonx Orchestrate—allowing participants to build and audit AI agents in hours. These aren't prototypes—they're fully scalable solutions already in action at IBM: reducing HR ticket backlog, accelerating incident resolution, preventing IT outages, speeding up financial decisions, and driving personalized customer experiences. 
It’s part innovation showcase, part learning campus, part launchpad—tailored for global impact.
              <br></br><br></br>
              True autonomy demands trust. IBM's industry-first governance and security suite—integrating watsonx.governance with Guardium AI Security—provides full oversight across AI agents' lifecycle.
Monitor your AI agents with a governed catalog, deploy automated red-teaming, detect unauthorized (“shadow”) agents, and enforce compliance across global frameworks—like the EU AI Act and ISO 42001—through a unified dashboard.
In short, IBM doesn't just give you autonomous AI—it empowers you to run it responsibly, safely, and at scale.
              <br></br><br></br>
              IBM isn't just talking about AI agents—it's showing them in action, scaling them globally, and governing them comprehensively.
              <br />
👉 Want to experience live demos?<br />
👉 Curious about industry use cases—from IT automation to finance, HR, and security?<br />
👉 Ready to join hands-on workshops at the Bengaluru center or online?<br /><br />

Talk with our experts to dive deeper into IBM's agentic future. The next wave of AI isn't coming—it's here, and it's proactive. Are you ready to ride it?
            </p>
          </div>
        </div>
      </div>
      </div>
    </div>
  );
}

export default App;
