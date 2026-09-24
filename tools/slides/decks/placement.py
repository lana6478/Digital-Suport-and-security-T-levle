"""
Where each deck's inline link goes on each page.

Maps deck file -> {page: [targets]}. A target is either:
  - a specification number such as "1.8", matched against the number (or
    number range, e.g. "1.8-1.9") at the start of a page's ## or ### heading;
  - "top", placing the link after the page's introduction (for a deck that
    covers the whole page);
  - any other string, matched against the start of a heading's text.

The link goes at the end of the section's text. If a deck's sections are not
next to each other on the page, the link appears after each group.
Pages not listed here still get the deck in the Teaching resources table.
"""

CP1 = "01-core-component/01-core-paper-1.md"
CP2 = "01-core-component/02-core-paper-2.md"
ESP = "01-core-component/03-employer-set-projects.md"
DIAG = "03-appendices/02-diagram-notation.md"
SP = "02-occupational-specialisms/"
DS1, DS2, DS3 = (SP + "digital-support/0%d" % i for i in (1, 2, 3))
DI1, DI2, DI3 = (SP + "digital-infrastructure/0%d" % i for i in (1, 2, 3))
NC1, NC2, NC3 = (SP + "network-cabling/0%d" % i for i in (1, 2, 3))
CS1, CS2, CS3 = (SP + "cyber-security/0%d" % i for i in (1, 2, 3))

# Page paths are completed below so the table stays readable.
_SUFFIX = {
    "01": "-security-procedures-and-controls.md",
    "03": "-sources-of-knowledge.md",
}
_PAGE2 = {
    "digital-support": "-software-and-os-support.md",
    "digital-infrastructure": "-physical-and-virtual-infrastructure.md",
    "network-cabling": "-cabling-installation-and-testing.md",
    "cyber-security": "-remediation-and-risk-assessment.md",
}


def _full(page):
    if page.endswith(".md"):
        return page
    spec, num = page.rsplit("/", 1)
    suffix = _SUFFIX.get(num) or _PAGE2[spec.split("/")[-1]]
    return page + suffix


def _r(a, b):
    """Numbers a to b inclusive within one content area, e.g. _r('1.1', '1.7')."""
    area, start = a.split(".")
    end = int(b.split(".")[1])
    return [f"{area}.{n}" for n in range(int(start), end + 1)]


_RAW = {
    # Core Paper 1
    "core/01-computational-thinking-algorithms-and-diagrams.pptx": {
        CP1: ["1.1", "1.2", "2.7"], DIAG: ["Why this matters for assessment"]},
    "core/02-problem-solving-strategies-and-reflective-practice.pptx": {CP1: ["1.3", "2.10"]},
    "core/03-networks-cabling-and-unified-communications.pptx": {CP1: _r("2.1", "2.3")},
    "core/04-supporting-and-testing-systems.pptx": {CP1: ["2.4", "2.5"]},
    "core/05-project-management-and-risk-assessment.pptx": {CP1: ["2.8", "2.9"]},
    "core/06-data-fundamentals.pptx": {CP1: _r("3.1", "3.6")},
    "core/07-data-quality-systems-and-analysis.pptx": {CP1: ["2.6"] + _r("3.7", "3.12")},
    # Core Paper 2
    "core/08-health-and-safety-in-digital-work.pptx": {CP2: ["4.1"]},
    "core/09-digital-legislation-and-professional-guidelines.pptx": {CP2: ["4.1", "4.2"]},
    "core/10-the-business-context.pptx": {CP2: _r("5.1", "5.3")},
    "core/11-technical-change-management.pptx": {CP2: ["5.4"]},
    "core/12-digital-support-roles-and-communication.pptx": {CP2: ["5.5"]},
    "core/13-emerging-issues-and-technologies.pptx": {CP2: ["6.1", "6.2"]},
    "core/14-hardware-and-software.pptx": {CP2: ["7.1", "7.2"]},
    "core/15-networks.pptx": {CP2: ["7.3"]},
    "core/16-virtual-cloud-and-resilient-environments.pptx": {CP2: _r("7.4", "7.6")},
    "core/17-security-threats-and-vulnerabilities.pptx": {CP2: ["8.1", "8.2"]},
    "core/18-threat-mitigation-cia-and-iaaa.pptx": {CP2: ["8.3", "8.4"]},
    "core/19-employer-set-project-overview.pptx": {ESP: ["Common structure across all three ESPs"]},
    # Shared security decks (numbering differs slightly per specialism)
    "shared/01-business-security-controls.pptx": {
        DS1: _r("1.1", "1.7"), DI1: _r("1.1", "1.7"), NC1: ["1.1", "1.2", "1.7"]},
    "shared/02-disaster-recovery-and-backup.pptx": {
        DS1: ["1.8", "1.11", "1.22"], DI1: ["1.8", "1.12", "1.23"], NC1: ["1.8", "1.21"],
        DI2: ["2.18"]},
    "shared/03-risk-management-and-threat-assessment.pptx": {
        DS1: ["1.9", "1.10"] + _r("1.12", "1.18") + ["1.20"],
        DI1: ["1.10", "1.11"] + _r("1.13", "1.19") + ["1.21"],
        NC1: ["1.9", "1.12", "1.15", "1.16", "1.20"]},
    "shared/04-technical-security-and-network-protection.pptx": {
        DS1: ["1.19", "1.21"] + _r("1.25", "1.28") + _r("1.30", "1.32"),
        DI1: ["1.20", "1.22"] + _r("1.26", "1.30") + ["1.32", "1.33"],
        NC1: ["1.19", "1.25", "1.31", "1.32"]},
    "shared/05-security-law-standards-and-policy.pptx": {
        DS1: ["1.23", "1.24", "1.29"], DI1: ["1.24", "1.25", "1.31"], NC1: ["1.24"]},
    "shared/06-sources-of-knowledge.pptx": {
        DS3: ["top"], DI3: ["top"], NC3: ["top"], CS3: ["top"], CP1: ["2.11"]},
    # Cyber Security
    "cyber-security/01-governance-itsm-and-frameworks.pptx": {
        CS1: ["1.1", "1.2", "1.7", "1.8", "1.10", "1.24"]},
    "cyber-security/02-secure-design-and-layered-protection.pptx": {CS1: _r("1.3", "1.6") + ["1.23"]},
    "cyber-security/03-security-controls-and-disaster-recovery.pptx": {CS1: _r("1.11", "1.16")},
    "cyber-security/04-cryptography-and-digital-certificates.pptx": {
        CS1: ["1.9"] + _r("1.17", "1.20"), CS2: ["2.22"]},
    "cyber-security/05-cyber-law-and-ethics.pptx": {CS1: ["1.21", "1.22"]},
    "cyber-security/06-threats-threat-actors-and-intelligence.pptx": {CS2: ["2.2", "2.3"], CS3: ["3.8"]},
    "cyber-security/07-vulnerability-assessment-and-penetration-testing.pptx": {
        CS2: ["2.4", "2.5", "2.6", "2.8", "2.9", "2.17"]},
    "cyber-security/08-risk-analysis-and-risk-response.pptx": {
        CS2: ["2.7", "2.10"] + _r("2.12", "2.16") + ["2.18"]},
    "cyber-security/09-incident-management-and-forensics.pptx": {CS2: ["2.1", "2.19", "2.20"]},
    "cyber-security/10-mitigation-backups-and-compliance.pptx": {
        CS2: ["2.11", "2.21", "2.23", "2.24", "2.25"]},
    # Digital Infrastructure
    "digital-infrastructure/01-network-design-addressing-and-transmission.pptx": {DI2: ["2.1", "2.2"]},
    "digital-infrastructure/02-infrastructure-components-and-cabling.pptx": {DI2: ["2.3", "2.15"]},
    "digital-infrastructure/03-servers-virtualisation-and-operating-systems.pptx": {DI2: ["2.6", "2.9", "2.23"]},
    "digital-infrastructure/04-network-services-remote-access-and-installation.pptx": {
        DI2: ["2.10", "2.11", "2.13"]},
    "digital-infrastructure/05-health-safety-and-esd.pptx": {DI2: ["2.4", "2.5"]},
    "digital-infrastructure/06-service-management-and-solution-lifecycle.pptx": {
        DI2: ["2.16", "2.20", "2.21", "2.22", "2.24"]},
    # Digital Support
    "digital-support/01-agile-values-and-methodologies.pptx": {DS2: ["2.1", "2.2"]},
    "digital-support/02-domains-email-and-remote-access.pptx": {DS2: ["2.4"] + _r("2.16", "2.20")},
    "digital-support/03-devices-operating-systems-and-applications.pptx": {DS2: _r("2.6", "2.9")},
    "digital-support/04-os-deployment-imaging-and-recovery.pptx": {DS2: _r("2.10", "2.15")},
    "digital-support/05-end-user-support-and-troubleshooting.pptx": {
        DS2: ["2.5"] + _r("2.21", "2.23") + ["2.28"]},
    "digital-support/06-asset-version-and-mobile-device-management.pptx": {DS2: _r("2.24", "2.26")},
    "digital-support/07-digital-solutions-and-training-users.pptx": {DS2: ["2.3", "2.27", "2.29"]},
    # Network Cabling
    "network-cabling/01-signal-theory-and-data-transmission.pptx": {NC2: ["2.1", "2.7", "2.10"]},
    "network-cabling/02-cable-media-connectors-and-standards.pptx": {
        NC2: ["2.11", "2.12", "2.13", "2.15", "2.16"]},
    "network-cabling/03-structured-cabling-design-and-installation.pptx": {
        NC2: ["2.2", "2.3", "2.5", "2.25"]},
    "network-cabling/04-testing-certification-and-troubleshooting.pptx": {NC2: ["2.17", "2.26", "2.29"]},
    "network-cabling/05-health-safety-and-compliance-for-cabling.pptx": {NC2: ["2.19", "2.22", "2.23"]},
}

PLACEMENT = {deck: {_full(p): t for p, t in pages.items()} for deck, pages in _RAW.items()}
