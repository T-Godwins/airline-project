# **The Digital Handshake**
## **Validating the CES 2025 Vision for Premium Airline Retention**

![Delta CEO Ed Bastian CES 2025](images/Ed_Bastian_at_CES_2025.jpg)
*(Delta CEO Ed Bastian at CES: "Technology is the lever to propel the next century of flight.")*

### **Executive Summary**
The airline industry relies on the **Business Class segment**, which represents just 12% of passengers but generates up to [75% of profits](https://www.investopedia.com/ask/answers/041315/how-much-revenue-airline-industry-comes-business-travelers-compared-leisure-travelers.asp). This project tests the CEO's hypothesis that "Human-Centric Tech" is the primary driver of retention for these high-value travelers.

**Key Findings:**
* **Digital > Physical:** Predictive modeling (94% accuracy) reveals that the **Digital Friction Index** (App, Wifi, Boarding) is a stronger predictor of premium churn than Seat Comfort.
* **The "Digital Handshake":** Business Class passengers punish app failures severely. A boarding rating of 3/5 is acceptable in Economy but creates a **Detractor Event** in Business.
* **Revenue Blocking:** Qualitative validation proved that app glitches are actively blocking paid upgrades, directly costing the airline revenue.

📄 **[Read the Full Executive Summary](EXECUTIVE_SUMMARY.md)**

---

### **Project Architecture**

| Component | Content Focus | Link |
| :--- | :--- | :--- |
| **The Narrative** | **Strategy.** A deeper dive into the "Expectation Gap" with "Digital Handshake". | [**View Story Notebook**](detailed_analysis/airline_sentiment_story.ipynb) |
| **The Code** | **Data Science.** Notebooks 01-04 covering Cleaning, Baseline Modeling, Feature Engineering, and Model Evaluation. | [**View Notebooks**](technical_analysis/) |
| **The Validation** | **AI Engineering.** A RAG pipeline using OpenAI & Pinecone to semantically search Reddit for qualitative evidence. | [**View Reddit Scraper**](technical_analysis/05_reddit_validation.ipynb) |

---

### **Technical Setup**
*(For developers looking to reproduce this analysis)*

**Installation**
```bash
git clone [https://github.com/yourusername/airline-sentiment-strategy.git](https://github.com/yourusername/airline-sentiment-strategy.git)
pip install -r requirements.txt
```

**API Keys** (Optional): For Notebook 05 (Reddit Validation), create a `.env.local` file with your Reddit, OpenAI, and Pinecone API keys - see [Reddit API](https://www.reddit.com/prefs/apps), [OpenAI API](https://platform.openai.com/api-keys), and [Pinecone](https://www.pinecone.io/) for setup instructions.