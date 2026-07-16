from dataclasses import dataclass, field
from typing import List


@dataclass
class Project:
    title: str
    description: str


@dataclass
class Education:
    degree: str
    institution: str
    cgpa: str = ""


@dataclass
class Experience:
    company: str
    role: str
    duration: str
    description: str


@dataclass
class Resume:

    name: str

    email: str

    phone: str

    target_role: str

    summary: str

    skills: List[str] = field(default_factory=list)

    projects: List[Project] = field(default_factory=list)

    education: List[Education] = field(default_factory=list)

    experience: List[Experience] = field(default_factory=list)

    certifications: List[str] = field(default_factory=list)